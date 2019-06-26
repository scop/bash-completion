import pytest


class TestChrpath:
    @pytest.mark.complete("chrpath ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("chrpath -", require_cmd=True)
    def test_2(self, completion):
        assert completion
