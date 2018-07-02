import pytest


class Test(object):

    @pytest.mark.complete("cut ")
    def test_(self, completion):
        assert completion.list
