import pytest


class Test(object):

    @pytest.mark.complete("postsuper ")
    def test_(self, completion):
        assert completion.list
