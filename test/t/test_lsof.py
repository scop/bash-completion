import pytest


class TestLsof:
    @pytest.mark.complete("lsof ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("lsof -")
    def test_2(self, completion):
        assert completion
