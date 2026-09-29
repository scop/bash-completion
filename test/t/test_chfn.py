import pytest


class TestChfn:
    @pytest.mark.complete("chfn ")
    def test_1(self, completion):
        assert completion
