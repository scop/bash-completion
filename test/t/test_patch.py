import pytest


class Test(object):

    @pytest.mark.complete("patch ")
    def test_(self, completion):
        assert completion.list
