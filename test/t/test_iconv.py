import pytest


class TestIconv(object):

    @pytest.mark.complete("iconv -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("iconv -f UTF")
    def test_2(self, completion):
        assert completion.list
