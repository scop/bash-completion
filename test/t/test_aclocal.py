import pytest


class Test(object):

    @pytest.mark.complete("aclocal ")
    def test_(self, completion):
        assert completion.list
