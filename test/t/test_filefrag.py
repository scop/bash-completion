import pytest


class Test(object):

    @pytest.mark.complete("filefrag ")
    def test_(self, completion):
        assert completion.list
