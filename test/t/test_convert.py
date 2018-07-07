import pytest


class TestConvert(object):

    @pytest.mark.complete("convert ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("convert -format ")
    def test_2(self, completion):
        assert completion.list
