import pytest


class Test(object):

    @pytest.mark.complete("awk ")
    def test_(self, completion):
        assert completion.list
