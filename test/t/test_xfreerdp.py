import pytest


class Test(object):

    @pytest.mark.complete("xfreerdp ")
    def test_(self, completion):
        assert completion.list
