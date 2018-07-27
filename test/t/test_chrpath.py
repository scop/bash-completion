import pytest


class TestChrpath:

    @pytest.mark.complete("chrpath ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("chrpath -")
    def test_2(self, completion):
        assert completion.list
