import pytest


class TestXev:
    @pytest.mark.complete("xev ")
    def test_basic(self, completion):
        assert not completion

    @pytest.mark.complete("xev -", require_cmd=True)
    def test_options(self, completion):
        assert completion
