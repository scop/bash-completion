import pytest


@pytest.mark.pre_commands(
    "HOME=$PWD/mplayer",
)
class TestMplayer(object):

    @pytest.mark.complete("mplayer ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("mplayer -h")
    def test_2(self, completion):
        assert completion.list
