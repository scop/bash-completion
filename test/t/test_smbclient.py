import pytest


class Test(object):

    @pytest.mark.complete("smbclient -")
    def test_dash(self, completion):
        assert completion.list
