import pytest


class TestLess:
    @pytest.mark.complete("less --", require_longopt=True)
    def test_1(self, completion):
        assert completion
