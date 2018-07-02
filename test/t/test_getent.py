import pytest


class Test(object):

    @pytest.mark.complete("getent ")
    def test_(self, completion):
        assert completion.list
