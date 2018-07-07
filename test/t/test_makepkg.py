import pytest


class Test(object):

    @pytest.mark.complete("makepkg ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("makepkg --")
    def test_dash(self, completion):
        assert completion.list == "--chown --linkadd --prepend".split()
