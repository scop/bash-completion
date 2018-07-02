import pytest


class Test(object):

    @pytest.mark.complete("mtx ")
    def test_(self, completion):
        assert completion.list
