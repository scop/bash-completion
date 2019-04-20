import pytest


class TestGeoiplookup:
    @pytest.mark.complete("geoiplookup -")
    def test_1(self, completion):
        assert completion
