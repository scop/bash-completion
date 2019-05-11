import pytest


class TestWsimport:
    @pytest.mark.complete("wsimport ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("wsimport -")
    def test_2(self, completion):
        assert completion
