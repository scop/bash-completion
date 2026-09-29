import pytest


class TestHash:
    @pytest.mark.complete("hash ", require_cmd=True)
    def test_basic(self, completion):
        assert completion

    @pytest.mark.complete("hash -", require_cmd=True)
    def test_options(self, completion):
        assert completion
