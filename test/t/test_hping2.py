import pytest


class TestHping2:
    @pytest.mark.complete("hping2 ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("hping2 -", require_cmd=True)
    def test_2(self, completion):
        assert completion
