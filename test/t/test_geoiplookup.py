import pytest


class TestGeoiplookup(object):

    @pytest.mark.complete("geoiplookup -")
    def test_1(self, completion):
        assert completion.list
