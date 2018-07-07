import pytest


class TestIpsec(object):

    @pytest.mark.complete("ipsec ")
    def test_1(self, completion):
        assert completion.list
