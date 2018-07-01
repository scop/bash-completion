import pytest


class Test(object):

    @pytest.mark.complete("od ")
    def test_(self, completion):
        assert completion.list
