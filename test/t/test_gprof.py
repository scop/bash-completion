import pytest


class TestGprof(object):

    @pytest.mark.complete("gprof --",
                          skipif="! gprof --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
