import pytest


class TestSmbclient(object):

    @pytest.mark.complete("smbclient -")
    def test_1(self, completion):
        assert completion.list
