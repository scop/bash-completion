import pytest


class TestPmPowersave(object):

    @pytest.mark.complete("pm-powersave ")
    def test_1(self, completion):
        assert completion.list
