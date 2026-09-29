import pytest


class TestMv:
    @pytest.mark.complete("mv ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mv -", require_longopt=True)
    def test_options(self, completion):
        assert completion
