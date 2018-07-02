import pytest


class Test(object):

    @pytest.mark.complete("hexdump -")
    def test_dash(self, completion):
        assert completion.list
