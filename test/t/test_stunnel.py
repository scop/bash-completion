import pytest


class TestStunnel:
    @pytest.mark.complete("stunnel ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("stunnel -", require_cmd=True)
    def test_2(self, completion):
        assert completion
