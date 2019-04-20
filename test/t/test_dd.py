import pytest


class TestDd:
    @pytest.mark.complete("dd --")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("dd bs")
    def test_2(self, completion):
        assert completion == "bs="
