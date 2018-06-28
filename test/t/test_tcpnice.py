import pytest


class Test(object):

    @pytest.mark.complete("tcpnice -")
    def test_dash(self, completion):
        assert completion.list
