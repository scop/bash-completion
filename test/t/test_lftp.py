import pytest


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD/lftp",))
class TestLftp:
    @pytest.mark.complete("lftp ")
    def test_1(self, bash, completion, output_sort_uniq):
        hosts = output_sort_uniq("compgen -A hostname")
        assert all(x in completion for x in hosts)
        assert "lftptest" in completion  # defined in lftp/.lftp/bookmarks

    @pytest.mark.complete("lftp -", require_cmd=True)
    def test_2(self, completion):
        assert completion
