import pytest


class TestFold:
    @pytest.mark.complete("fold --", require_longopt=True)
    def test_1(self, completion):
        assert completion
