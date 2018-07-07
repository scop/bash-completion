import pytest


class TestPvremove(object):

    @pytest.mark.complete("pvremove --",
                          skipif="! pvremove --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
