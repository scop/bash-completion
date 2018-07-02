import pytest


class Test(object):

    @pytest.mark.complete("geoiplookup -")
    def test_dash(self, completion):
        assert completion.list
