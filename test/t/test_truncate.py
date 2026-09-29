import pytest


class TestTruncate:
    @pytest.mark.complete("truncate ")
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("truncate -", require_cmd=True)
    def test_options(self, completion):
        assert completion
