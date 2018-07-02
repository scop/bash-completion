import pytest


class Test(object):

    @pytest.mark.complete("pyvenv ")
    def test_(self, completion):
        assert completion.list
