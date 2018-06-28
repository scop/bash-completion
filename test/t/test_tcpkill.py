import pytest


class Test(object):

    @pytest.mark.complete("tcpkill -")
    def test_dash(self, completion):
        assert completion.list
