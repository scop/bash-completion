import pytest


class TestBzip2(object):

    @pytest.mark.complete("bzip2 ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("bzip2 ~")
    def test_2(self, completion):
        assert completion.list
