import pytest


class Test(object):

    @pytest.mark.complete("jarsigner ")
    def test_(self, completion):
        assert completion.list
