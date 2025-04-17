import pytest


class TestShtab:
    @pytest.mark.complete("shtab ", require_cmd=True)
    def test_basic(self, completion):
        assert not completion

    @pytest.mark.complete("shtab -", require_cmd=True)
    def test_options(self, completion):
        assert completion
