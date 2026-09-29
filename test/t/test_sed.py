import pytest


class TestSed:
    @pytest.mark.complete("sed --", require_longopt=True)
    def test_1(self, completion):
        assert completion
