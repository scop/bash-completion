import pytest


class Test(object):

    @pytest.mark.complete("abook -")
    def test_dash(self, completion):
        assert completion.list
