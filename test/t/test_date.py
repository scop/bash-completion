import pytest


class TestDate:
    @pytest.mark.complete("date ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("date -", require_cmd=True)
    def test_options(self, completion):
        assert completion
