import pytest


class TestLdd(object):

    @pytest.mark.complete("ldd ")
    def test_1(self, completion):
        assert completion.list
