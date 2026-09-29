import pytest


@pytest.mark.bashcomp(cmd="mii-diag")
class TestMiiDiag:
    @pytest.mark.complete("mii-diag ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("mii-diag -", require_cmd=True)
    def test_2(self, completion):
        assert completion
