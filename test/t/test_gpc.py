import pytest


class TestGpc(object):

    @pytest.mark.complete("gpc ")
    def test_1(self, completion):
        assert completion.list
