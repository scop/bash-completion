import pytest


class TestCut:
    @pytest.mark.complete("cut ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cut -", require_longopt=True)
    def test_options(self, completion):
        assert completion
