import pytest


class TestNetstat(object):

    @pytest.mark.complete("netstat ")
    def test_1(self, completion):
        assert completion.list
