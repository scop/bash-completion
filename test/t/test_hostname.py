import pytest


class Test(object):

    @pytest.mark.complete("hostname -")
    def test_dash(self, completion):
        assert completion.list
