import pytest


class TestXgamma:
    @pytest.mark.complete("xgamma -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xgamma -gam", require_cmd=True)
    def test_2(self, completion):
        assert completion == "ma"
        assert completion.endswith(" ")
