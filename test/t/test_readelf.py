import pytest


class TestReadelf:
    @pytest.mark.complete("readelf --")
    def test_1(self, completion):
        assert completion
