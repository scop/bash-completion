import pytest


class TestLzma:

    @pytest.mark.complete("lzma ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("lzma -")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("lzma -d xz/")
    def test_3(self, completion):
        assert completion.list == "a/ bashcomp.lzma bashcomp.tlz".split()

    @pytest.mark.complete("lzma ~")
    def test_4(self, completion):
        assert completion.list
