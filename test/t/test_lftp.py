import pytest


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD/lftp",))
class TestLftp:
    @pytest.mark.complete("lftp ", require_cmd=True)
    def test_1(self, bash, completion, output_sort_uniq):
        hosts = output_sort_uniq("compgen -A hostname")
        assert all(x in completion for x in hosts)
        # defined in lftp/.lftp/bookmarks
        assert all(x in completion for x in "lftptest spacetest".split())
        assert "badbookmark" not in completion

    @pytest.mark.complete("lftp -", require_cmd=True)
    def test_2(self, completion):
        assert completion
