import pytest


@pytest.mark.bashcomp(
    cmd="locale-gen",
)
class TestLocaleGen:

    @pytest.mark.complete("locale-gen ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("locale-gen --")
    def test_2(self, completion):
        assert completion.list
