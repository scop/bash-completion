import pytest


class TestOd:
    @pytest.mark.complete("od ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("od -", require_longopt=True)
    def test_options(self, completion):
        assert completion
