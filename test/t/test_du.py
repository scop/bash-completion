import pytest


class TestDu:
    @pytest.mark.complete("du ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("du -", require_longopt=True)
    def test_options(self, completion):
        assert completion
