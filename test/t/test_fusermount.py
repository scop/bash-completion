import pytest


class Test(object):

    @pytest.mark.complete("fusermount ")
    def test_(self, completion):
        assert completion.list
