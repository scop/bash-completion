import pytest


class TestShuf:
    @pytest.mark.complete("shuf ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("shuf -", require_longopt=True)
    def test_options(self, completion):
        assert completion
