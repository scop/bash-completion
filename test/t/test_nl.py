import pytest


class Test(object):

    @pytest.mark.complete("nl ")
    def test_(self, completion):
        assert completion.list
