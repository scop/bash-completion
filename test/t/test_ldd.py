import pytest


class Test(object):

    @pytest.mark.complete("ldd ")
    def test_(self, completion):
        assert completion.list
