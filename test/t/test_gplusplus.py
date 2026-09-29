import pytest


@pytest.mark.bashcomp(cmd="g++")
class TestGPlusPlus:
    @pytest.mark.complete("g++ ")
    def test_1(self, completion):
        assert completion
