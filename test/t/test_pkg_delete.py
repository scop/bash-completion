import pytest


class Test(object):

    @pytest.mark.complete("pkg_delete ")
    def test_(self, completion):
        assert completion.list
