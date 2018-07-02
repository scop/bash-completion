import pytest


class Test(object):

    @pytest.mark.complete("fbi ")
    def test_(self, completion):
        assert completion.list
