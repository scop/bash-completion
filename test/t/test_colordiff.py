import pytest


class TestColordiff:
    @pytest.mark.complete("colordiff ")
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("colordiff -", require_cmd=True)
    def test_options(self, completion):
        assert completion
