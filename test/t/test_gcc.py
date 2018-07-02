import pytest


class Test(object):

    @pytest.mark.complete("gcc ")
    def test_(self, completion):
        assert completion.list
