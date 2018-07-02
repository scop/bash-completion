import pytest


class Test(object):

    @pytest.mark.complete("lpq ")
    def test_(self, completion):
        assert completion.list
