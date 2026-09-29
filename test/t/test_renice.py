import pytest


class TestRenice:
    @pytest.mark.complete("renice 1")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("renice -g ")
    def test_2(self, completion):
        assert completion
