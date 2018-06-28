import pytest


class Test(object):

    @pytest.mark.complete("tcpdump -")
    def test_dash(self, completion):
        assert completion.list
