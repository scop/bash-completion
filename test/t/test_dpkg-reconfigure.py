import pytest


class Test(object):

    @pytest.mark.complete("dpkg-reconfigure --")
    def test_dash(self, completion):
        assert completion.list
