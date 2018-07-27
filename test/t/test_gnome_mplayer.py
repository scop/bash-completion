import pytest


@pytest.mark.bashcomp(
    cmd="gnome-mplayer",
)
class TestGnomeMplayer:

    @pytest.mark.complete("gnome-mplayer ")
    def test_1(self, completion):
        assert completion.list
