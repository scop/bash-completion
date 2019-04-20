import pytest


class TestWsimport:
    @pytest.mark.complete("wsimport ")
    def test_1(self, completion):
        assert completion
