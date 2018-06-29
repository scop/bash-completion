import pytest


class Test(object):

    @pytest.mark.complete("smbget -")
    def test_dash(self, completion):
        assert completion.list
