import pytest


class Test(object):

    @pytest.mark.complete("pwck ")
    def test_(self, completion):
        assert completion.list
