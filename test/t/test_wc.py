import pytest


class TestWc:
    @pytest.mark.complete("wc --", require_longopt=True)
    def test_1(self, completion):
        assert completion
