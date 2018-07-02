import pytest


class Test(object):

    @pytest.mark.complete("chpasswd -")
    def test_dash(self, completion):
        assert completion.list
