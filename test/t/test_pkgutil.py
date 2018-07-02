import pytest


class Test(object):

    @pytest.mark.complete("pkgutil ")
    def test_(self, completion):
        assert completion.list
