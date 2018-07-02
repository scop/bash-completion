import pytest


class Test(object):

    @pytest.mark.complete("eog ")
    def test_(self, completion):
        assert completion.list
