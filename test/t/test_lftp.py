import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(
    pre_cmds=(
        "HOME=$PWD/lftp",
    ),
)
class TestLftp:

    @pytest.mark.complete("lftp ")
    def test_1(self, bash, completion):
        hosts = assert_bash_exec(
            bash, "compgen -A hostname", want_output=True).split()
        for host in hosts:
            assert host in completion.list
        assert "lftptest" in completion.list  # defined in lftp/.lftp/bookmarks
