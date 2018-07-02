import pytest


class Test(object):

    @pytest.mark.complete("htop -")
    def test_dash(self, completion):
        assert completion.list
