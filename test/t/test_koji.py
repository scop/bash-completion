import pytest


class TestKoji:
    @pytest.mark.complete("koji ", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("koji -", require_cmd=True)
    def test_2(self, completion):
        assert completion
