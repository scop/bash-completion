import pytest


class Test(object):

    @pytest.mark.complete("pkg-get ")
    def test_(self, completion):
        assert completion.list
