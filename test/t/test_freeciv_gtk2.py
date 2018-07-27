import pytest


@pytest.mark.bashcomp(
    cmd="freeciv-gtk2",
)
class TestFreecivGtk2:

    @pytest.mark.complete("freeciv-gtk2 -")
    def test_1(self, completion):
        assert completion.list
