import pytest


class Test(object):

    @pytest.mark.complete("smbtar -")
    def test_dash(self, completion):
        assert completion.list
