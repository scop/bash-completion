import pytest


class TestRealpath:
    @pytest.mark.complete("realpath ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("realpath -", require_longopt=True)
    def test_options(self, completion):
        assert completion
