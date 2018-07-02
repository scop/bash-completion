import pytest


class Test(object):

    @pytest.mark.complete("mogrify ")
    def test_(self, completion):
        assert completion.list
