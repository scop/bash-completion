import pytest


class Test(object):

    @pytest.mark.complete("hciattach ")
    def test_(self, completion):
        assert completion.list
