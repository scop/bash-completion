import pytest


class TestNumfmt:
    @pytest.mark.complete("numfmt ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("numfmt -", require_longopt=True)
    def test_options(self, completion):
        assert completion
