import pytest


class TestSmbpasswd(object):

    @pytest.mark.complete("smbpasswd -")
    def test_1(self, completion):
        assert completion.list
