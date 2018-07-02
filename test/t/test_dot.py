import pytest


class Test(object):

    @pytest.mark.complete("dot ")
    def test_(self, completion):
        assert completion.list
