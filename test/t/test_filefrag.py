import pytest


class TestFilefrag:
    @pytest.mark.complete("filefrag ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("filefrag -")
    def test_2(self, completion):
        assert completion
