import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        "HOME=$PWD/mplayer",
    ),
)
class TestMencoder(object):

    @pytest.mark.complete("mencoder ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("mencoder -v")
    def test_2(self, completion):
        assert completion.list
