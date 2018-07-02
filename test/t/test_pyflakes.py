import pytest


class Test(object):

    @pytest.mark.complete("pyflakes ")
    def test_(self, completion):
        assert completion.list
