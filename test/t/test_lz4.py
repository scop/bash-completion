import pytest


class TestLz4:
    @pytest.mark.complete("lz4 ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("lz4 ~")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("lz4 -", require_cmd=True)
    def test_3(self, completion):
        assert completion
