import pytest


class Test(object):

    @pytest.mark.complete("ypcat ")
    def test_(self, completion):
        assert completion.list
