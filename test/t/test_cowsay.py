import pytest


class Test(object):

    @pytest.mark.complete("cowsay ")
    def test_(self, completion):
        assert completion.list
