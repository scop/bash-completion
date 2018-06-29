import pytest


class Test(object):

    @pytest.mark.complete("smbpasswd -")
    def test_dash(self, completion):
        assert completion.list
