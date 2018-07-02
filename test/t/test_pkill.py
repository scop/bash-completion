import pytest


class Test(object):

    @pytest.mark.complete("pkill ")
    def test_(self, completion):
        assert completion.list
