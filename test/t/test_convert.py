import pytest


class Test(object):

    @pytest.mark.complete("convert ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("convert -format ")
    def test_format(self, completion):
        assert completion.list
