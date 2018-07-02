import pytest


class Test(object):

    @pytest.mark.complete("irb ")
    def test_(self, completion):
        assert completion.list
