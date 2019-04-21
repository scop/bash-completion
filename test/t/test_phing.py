import pytest


class TestPhing:
    @pytest.mark.complete("phing -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("phing -l ")
    def test_2(self, completion):
        assert not completion
