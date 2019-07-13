import pytest


class TestTail:
    @pytest.mark.complete("tail --", require_longopt=True)
    def test_1(self, completion):
        assert completion
