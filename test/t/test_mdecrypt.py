import pytest


class Test(object):

    @pytest.mark.complete("mdecrypt ")
    def test_(self, completion):
        assert completion.list
