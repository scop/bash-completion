import pytest


class TestBasenc:
    @pytest.mark.complete("basenc ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("basenc -", require_longopt=True)
    def test_options(self, completion):
        assert completion
