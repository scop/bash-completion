import pytest


class TestFree:
    @pytest.mark.complete("free ")
    def test_basic(self, completion):
        assert not completion

    @pytest.mark.complete("free -", require_cmd=True)
    def test_options(self, completion):
        assert completion
