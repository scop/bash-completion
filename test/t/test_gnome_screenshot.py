import pytest


@pytest.mark.bashcomp(
    cmd="gnome-screenshot",
)
class TestGnomeScreenshot:

    @pytest.mark.complete("gnome-screenshot --help")
    def test_1(self, completion):
        assert completion.list
