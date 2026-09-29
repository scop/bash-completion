import pytest


class TestHead:
    @pytest.mark.complete("head --", require_longopt=True)
    def test_1(self, completion):
        assert completion
