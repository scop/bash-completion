import re

import pexpect
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
        cmd = "cd shared/default/foo\002\002\002"  # \002 = ^B = cursor left
        bash.send(cmd + "\t")
        bash.expect_exact(cmd.replace("\002", "\b"))
        bash.send(MAGIC_MARK)
        bash.expect(
            r"\r\nbar bar\.d/\s+foo\.d/\r\n"
            + re.escape(PS1 + cmd.replace("\002", "\b") + MAGIC_MARK)
            + "foo\b\b\b"
        )
