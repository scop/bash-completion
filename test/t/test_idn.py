import pytest


class Test(object):

    @pytest.mark.complete("idn -")
    def test_dash(self, completion):
        assert completion.list
