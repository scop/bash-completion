import pytest


class Test(object):

    @pytest.mark.complete("gprof --",
                          skipif="! gprof --help &>/dev/null")
    def test_dash(self, completion):
        assert completion.list
