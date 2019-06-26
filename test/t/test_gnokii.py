import pytest


class TestGnokii:
    @pytest.mark.complete("gnokii ", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("gnokii -", require_cmd=True)
    def test_2(self, completion):
        assert completion
