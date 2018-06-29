import pytest


class Test(object):

    @pytest.mark.complete("sshow -")
    def test_dash(self, completion):
        assert completion.list
