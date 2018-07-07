import pytest


class TestTcpkill(object):

    @pytest.mark.complete("tcpkill -")
    def test_1(self, completion):
        assert completion.list
