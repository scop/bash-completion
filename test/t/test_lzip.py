import pytest


class TestLzip:

    @pytest.mark.complete("lzip ")
    def test_1(self, completion):
        assert completion.list
