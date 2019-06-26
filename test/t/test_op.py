import pytest


class TestOp:
    @pytest.mark.complete("op ", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("op --", require_cmd=True)
    def test_2(self, completion):
        assert completion
