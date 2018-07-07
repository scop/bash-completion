import pytest


class TestLuseradd(object):

    @pytest.mark.complete("luseradd -")
    def test_1(self, completion):
        assert completion.list
