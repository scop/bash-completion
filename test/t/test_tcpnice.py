import pytest


class TestTcpnice(object):

    @pytest.mark.complete("tcpnice -")
    def test_1(self, completion):
        assert completion.list
