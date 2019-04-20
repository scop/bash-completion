import pytest


@pytest.mark.bashcomp(cmd="c++")
class TestCPlusPlus:
    @pytest.mark.complete("c++ ")
    def test_1(self, completion):
        assert completion
