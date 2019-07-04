import pytest


class TestCsplit:
    @pytest.mark.complete("csplit ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("csplit -", require_cmd=True)
    def test_options(self, completion):
        assert completion
