import pytest


class Test(object):

    @pytest.mark.complete("svn ")
    def test_(self, completion):
        assert completion.list
