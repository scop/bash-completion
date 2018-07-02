import pytest


class Test(object):

    @pytest.mark.complete("jar ")
    def test_(self, completion):
        assert completion.list
