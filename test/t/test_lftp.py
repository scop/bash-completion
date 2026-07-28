import pytest


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD/lftp",))
class TestLftp:
    @pytest.mark.complete("lftp ", require_cmd=True)
    def test_1(self, bash, hosts_from_hostfile, completion, output_sort_uniq):
        assert all(x in completion for x in hosts_from_hostfile)
        # defined in lftp/.lftp/bookmarks
        assert all(x in completion for x in "lftptest spacetest".split())
        assert "badbookmark" not in completion

    @pytest.mark.complete("lftp -", require_cmd=True)
    def test_2(self, completion):
        assert completion
