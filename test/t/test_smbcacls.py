import pytest


class TestSmbcacls(object):

    @pytest.mark.complete("smbcacls -")
    def test_1(self, completion):
        assert completion.list
