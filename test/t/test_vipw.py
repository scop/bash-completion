import pytest


class Test(object):

    @pytest.mark.complete("vipw -")
    def test_dash(self, completion):
        assert completion.list
