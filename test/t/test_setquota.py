import pytest


class Test(object):

    @pytest.mark.complete("setquota ")
    def test_(self, completion):
        assert completion.list
