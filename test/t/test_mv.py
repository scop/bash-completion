import pytest


class Test(object):

    @pytest.mark.complete("mv ")
    def test_(self, completion):
        assert completion.list
