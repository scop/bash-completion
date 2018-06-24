import pytest


class Test(object):

    @pytest.mark.complete("pkgadd ")
    def test_(self, completion):
        assert completion.list
