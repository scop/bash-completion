import pytest


class Test(object):

    @pytest.mark.complete("service ")
    def test_(self, completion):
        assert completion.list
