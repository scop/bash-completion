import pytest


class TestTac:
    @pytest.mark.complete("tac --", require_longopt=True)
    def test_1(self, completion):
        assert completion
