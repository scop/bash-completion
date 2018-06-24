import pytest


class Test(object):

    @pytest.mark.complete("yum -")
    def test_dash(self, completion):
        assert completion.list
