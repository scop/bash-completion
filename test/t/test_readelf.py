import pytest


class TestReadelf(object):

    @pytest.mark.complete("readelf --")
    def test_1(self, completion):
        assert completion.list
