import pytest


class TestFmt(object):

    @pytest.mark.complete("fmt -",
                          skipif="! fmt --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
