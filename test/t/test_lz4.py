import pytest


class TestLz4(object):

    @pytest.mark.complete("lz4 ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("lz4 ~")
    def test_2(self, completion):
        assert completion.list
