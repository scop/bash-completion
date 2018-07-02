import pytest


class Test(object):

    @pytest.mark.complete("a2ps ")
    def test_(self, completion):
        assert completion.list
