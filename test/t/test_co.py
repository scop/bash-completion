import pytest


class Test(object):

    @pytest.mark.complete("co ")
    def test_(self, completion):
        assert completion.list
