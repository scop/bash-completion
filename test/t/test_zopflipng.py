import pytest


class TestZopflipng:
    @pytest.mark.complete("zopflipng ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("zopflipng -", require_cmd=True)
    def test_2(self, completion):
        assert completion
