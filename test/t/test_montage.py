import pytest


class Test(object):

    @pytest.mark.complete("montage ")
    def test_(self, completion):
        assert completion.list
