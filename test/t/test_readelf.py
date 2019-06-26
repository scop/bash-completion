import pytest


class TestReadelf:
    @pytest.mark.complete("readelf --", require_cmd=True)
    def test_1(self, completion):
        assert completion
