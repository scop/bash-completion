import pytest


class Test(object):

    @pytest.mark.complete("zopflipng ")
    def test_(self, completion):
        assert completion.list
