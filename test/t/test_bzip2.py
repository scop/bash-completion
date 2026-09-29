import pytest


class TestBzip2:
    @pytest.mark.complete("bzip2 ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("bzip2 ~")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("bzip2 -")
    def test_3(self, completion):
        assert completion
