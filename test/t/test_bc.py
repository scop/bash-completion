import pytest


class TestBc:
    @pytest.mark.complete("bc --", require_longopt=True)
    def test_1(self, completion):
        assert completion
