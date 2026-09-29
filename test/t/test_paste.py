import pytest


class TestPaste:
    @pytest.mark.complete("paste ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("paste -", require_longopt=True)
    def test_options(self, completion):
        assert completion
