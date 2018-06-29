import pytest


class Test(object):

    @pytest.mark.complete("strace -")
    def test_dash(self, completion):
        assert completion.list
