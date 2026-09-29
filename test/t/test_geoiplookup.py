import pytest


class TestGeoiplookup:
    @pytest.mark.complete("geoiplookup -", require_cmd=True)
    def test_1(self, completion):
        assert completion
