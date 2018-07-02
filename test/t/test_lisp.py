import pytest


class Test(object):

    @pytest.mark.complete("lisp ")
    def test_(self, completion):
        assert completion.list
