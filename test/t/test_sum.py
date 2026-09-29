import pytest


class TestSum:
    @pytest.mark.complete("sum ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("sum --", require_longopt=True)
    def test_options(self, completion):
        assert completion
