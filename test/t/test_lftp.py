import pytest

from conftest import assert_bash_exec


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD/lftp",))
class TestLftp:
    @pytest.mark.complete("lftp ")
    def test_1(self, bash, completion):
        hosts = assert_bash_exec(
            bash, "compgen -A hostname", want_output=True
        ).split()
        assert all(x in completion for x in hosts)
        assert "lftptest" in completion  # defined in lftp/.lftp/bookmarks

    @pytest.mark.complete("lftp -")
    def test_2(self, completion):
        assert completion
