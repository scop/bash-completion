import pytest


@pytest.mark.bashcomp(pre_cmds=("HOME=$PWD/mplayer",))
class TestMencoder:
    @pytest.mark.complete("mencoder ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mencoder -v", require_cmd=True)
    def test_2(self, completion):
        assert completion
