import pytest


class TestCat:
    @pytest.mark.complete("cat ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("cat -", require_longopt=True)
    def test_options(self, completion):
        assert completion
