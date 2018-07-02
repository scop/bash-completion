import pytest


class Test(object):

    @pytest.mark.complete("file-roller ")
    def test_(self, completion):
        assert completion.list
