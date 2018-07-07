import pytest


class TestTcpdump(object):

    @pytest.mark.complete("tcpdump -")
    def test_1(self, completion):
        assert completion.list
