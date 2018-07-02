import pytest


class Test(object):

    @pytest.mark.complete("insmod ")
    def test_(self, completion):
        assert completion.list
