import pytest


class Test(object):

    @pytest.mark.complete("gcj ")
    def test_(self, completion):
        assert completion.list
