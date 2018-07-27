import pytest


class TestXz:

    @pytest.mark.complete("xz ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("xz -d xz/")
    def test_2(self, completion):
        assert completion.list == "a/ bashcomp.lzma bashcomp.tar.xz " \
            "bashcomp.tlz bashcomp.xz".split()

    @pytest.mark.complete("xz xz/")
    def test_3(self, completion):
        assert completion.list == "a/ bashcomp.tar".split()

    @pytest.mark.complete("xz ~")
    def test_4(self, completion):
        assert completion.list
