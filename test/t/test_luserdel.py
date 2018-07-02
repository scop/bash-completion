import pytest


class Test(object):

    @pytest.mark.complete("luserdel ")
    def test_(self, completion):
        assert completion.list
