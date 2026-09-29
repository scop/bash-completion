import pytest


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD/mplayer",))
class TestMplayer:
    @pytest.mark.complete("mplayer ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mplayer -h", require_cmd=True)
    def test_2(self, completion):
        assert completion
