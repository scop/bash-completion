import pytest


class Test(object):

    @pytest.mark.complete("paste ")
    def test_(self, completion):
        assert completion.list
