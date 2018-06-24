import pytest


class Test(object):

    @pytest.mark.complete("xzdec ")
    def test_(self, completion):
        assert completion.list
