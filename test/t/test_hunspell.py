import pytest


class TestHunspell:

    @pytest.mark.complete("hunspell ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("hunspell -")
    def test_2(self, completion):
        assert completion.list
