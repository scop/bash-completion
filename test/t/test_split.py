import pytest


class TestSplit:
    @pytest.mark.complete("split --", require_longopt=True)
    def test_1(self, completion):
        assert completion
