import pytest


class Test(object):

    @pytest.mark.complete("vgscan -",
                          skipif="! vgscan --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
