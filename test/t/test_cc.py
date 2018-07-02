import pytest


class Test(object):

    @pytest.mark.complete("cc ")
    def test_(self, completion):
        assert completion.list
