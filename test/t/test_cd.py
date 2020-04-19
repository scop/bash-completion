import re

import pytest

from conftest import MAGIC_MARK, PS1


@pytest.mark.bashcomp(ignore_env=r"^\+CDPATH=$")
class TestCd:
    @pytest.mark.complete("cd shared/default/")
    def test_1(self, completion):
        assert completion == ["bar bar.d/", "foo.d/"]

    @pytest.mark.complete("cd fo", env=dict(CDPATH="shared/default"))
    def test_2(self, completion):
        assert completion == "foo.d/"

    @pytest.mark.complete("cd fo")
    def test_3(self, completion):
        assert not completion

    @pytest.mark.complete(
        "cd ", cwd="shared/default/foo.d", env=dict(CDPATH="")
    )
    def test_4(self, completion):
        assert not completion  # No subdirs nor CDPATH

    def test_dir_at_point(self, bash):
        trail = "foo"
        cmd = "cd shared/default/%s%s" % (
            trail,
            "\002" * len(trail),  # \002 = ^B = cursor left
        )
        bash.send(cmd + "\t")
        bash.expect_exact(cmd.replace("\002", "\b"))
        bash.send(MAGIC_MARK)
        bash.expect(r"\r\nbar bar\.d/\s+foo\.d/\r\n")
        bash.expect_exact(PS1 + cmd.replace("\002", "\b"))

        # At this point, something weird happens. For most test setups, as
        # expected (pun intended!), MAGIC_MARK follows as is. But for some
        # others (e.g. CentOS 6, Ubuntu 14 test containers), we get MAGIC_MARK
        # one character a time, followed each time by foo\b\b\b. Don't know
        # why, but accept it until/if someone finds out. Or just be fine with
        # it indefinitely, the visible and practical end result on a terminal
        # is the same anyway.
        repeat = "(%s%s)?" % (re.escape(trail), "\b" * len(trail))
        expected = "".join("%s%s" % (re.escape(x), repeat) for x in MAGIC_MARK)
        bash.expect(expected)
