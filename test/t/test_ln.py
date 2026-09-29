import pytest


class TestLn:
    @pytest.mark.complete("ln ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ln -", require_longopt=True)
    def test_options(self, completion):
        assert completion
