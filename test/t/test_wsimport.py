import pytest


class Test(object):

    @pytest.mark.complete("wsimport ")
    def test_(self, completion):
        assert completion.list
