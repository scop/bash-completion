import pytest


class Test(object):

    @pytest.mark.complete("ntpdate -")
    def test_dash(self, completion):
        assert completion.list
