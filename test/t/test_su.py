import pytest


class TestSu:
    @pytest.mark.complete("su ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("su -", require_cmd=True)
    def test_2(self, completion):
        assert completion
