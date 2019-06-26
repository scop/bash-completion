import pytest


class TestIftop:
    @pytest.mark.complete("iftop ", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("iftop -", require_cmd=True)
    def test_2(self, completion):
        assert completion
