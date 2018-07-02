import pytest


class Test(object):

    @pytest.mark.complete("postfix ")
    def test_(self, completion):
        assert completion.list
