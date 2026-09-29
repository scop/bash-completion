import os.path

import pytest

from conftest import assert_complete, is_bash_type


@pytest.mark.bashcomp(cmd="slapt-get")
class TestSlaptGet:
    @pytest.fixture(scope="class")
    def slapt_getrc(self, bash, tmp_path_factory):
        working_dir = os.path.join(
            bash.cwd, *"slackware var slapt-get".split()
        )

        tmpdir = tmp_path_factory.mktemp(
            "bash-completion._comp_cmd_slapt_get."
        )
        tmpfile = tmpdir / "slapt-getrc.0"
        tmpfile.write_text(
            f"WORKINGDIR={working_dir}/\nSOURCE=file:///home/\n"
        )
        return str(tmpfile)

    @pytest.mark.complete("slapt-get -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("slapt-get --up", require_cmd=True)
    def test_2(self, completion):
        assert completion == "--update --upgrade".split()

    @pytest.mark.complete("slapt-get -c non-existent-file --install ")
    def test_3(self, completion):
        assert not completion

    def test_install(self, bash, slapt_getrc):
        if not is_bash_type(bash, "slapt-get"):
            pytest.skip("slapt-get not found")
        completion = assert_complete(
            bash, "slapt-get -c %s --install " % slapt_getrc
        )
        assert completion == sorted(
            "abc-4-i686-1 ran-1.2-noarch-1 qwe-2.1-i486-1".split()
        )
