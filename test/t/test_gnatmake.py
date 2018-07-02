import pytest


class Test(object):

    @pytest.mark.complete("gnatmake ")
    def test_(self, completion):
        assert completion.list
