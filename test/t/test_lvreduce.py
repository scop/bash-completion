import pytest


class Test(object):

    @pytest.mark.complete("lvreduce --",
                          skipif="! lvreduce --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
