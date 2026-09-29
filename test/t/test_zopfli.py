import pytest


class TestZopfli:
    @pytest.mark.complete("zopfli ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("zopfli ~")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("zopfli -", require_cmd=True)
    def test_3(self, completion):
        assert completion
