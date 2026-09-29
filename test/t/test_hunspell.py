import pytest


class TestHunspell:
    @pytest.mark.complete("hunspell ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("hunspell -", require_cmd=True)
    def test_2(self, completion):
        assert completion
