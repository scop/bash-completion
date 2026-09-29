import pytest


class TestB2sum:
    @pytest.mark.complete("b2sum ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("b2sum --", require_longopt=True)
    def test_options(self, completion):
        assert completion
