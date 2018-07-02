import pytest


class Test(object):

    @pytest.mark.complete("mock ")
    def test_(self, completion):
        assert completion.list
