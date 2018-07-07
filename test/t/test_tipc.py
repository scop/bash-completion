import pytest


class TestTipc(object):

    @pytest.mark.complete("tipc ")
    def test_1(self, completion):
        assert completion.list
