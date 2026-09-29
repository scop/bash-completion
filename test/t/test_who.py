import pytest


class TestWho:
    @pytest.mark.complete("who --", require_longopt=True)
    def test_1(self, completion):
        assert completion
