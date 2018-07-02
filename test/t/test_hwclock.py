import pytest


class Test(object):

    @pytest.mark.complete("hwclock -")
    def test_dash(self, completion):
        assert completion.list
