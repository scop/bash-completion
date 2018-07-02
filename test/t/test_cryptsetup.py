import pytest


class Test(object):

    @pytest.mark.complete("cryptsetup ")
    def test_(self, completion):
        assert completion.list
