import pytest


class Test(object):

    @pytest.mark.complete("dpkg-source -")
    def test_dash(self, completion):
        assert completion.list
