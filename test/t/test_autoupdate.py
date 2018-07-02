import pytest


class Test(object):

    @pytest.mark.complete("autoupdate ")
    def test_(self, completion):
        assert completion.list
