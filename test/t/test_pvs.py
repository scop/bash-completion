import pytest


class TestPvs(object):

    @pytest.mark.complete("pvs --",
                          skipif="! pvs --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
