import pytest


class Test(object):

    @pytest.mark.complete("growisofs ")
    def test_(self, completion):
        assert completion.list
