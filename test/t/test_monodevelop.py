import pytest


class Test(object):

    @pytest.mark.complete("monodevelop ")
    def test_(self, completion):
        assert completion.list
