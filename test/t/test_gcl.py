import pytest


class Test(object):

    @pytest.mark.complete("gcl ")
    def test_(self, completion):
        assert completion.list
