import pytest


class TestTimeout:
    @pytest.mark.complete("timeout ")
    def test_1(self, completion):
        assert not completion

    @pytest.mark.complete("timeout -", require_cmd=True)
    def test_2(self, completion):
        assert completion
