import pytest


class Test(object):

    @pytest.mark.complete("fold --",
                          skipif="! fold --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
