import pytest


class TestLs:

    @pytest.mark.complete("ls --", skipif="! ls --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("ls ~")
    def test_2(self, completion):
        assert completion.list
