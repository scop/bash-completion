import pytest


class TestMakepkg(object):

    @pytest.mark.complete("makepkg ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("makepkg --")
    def test_2(self, completion):
        assert completion.list == "--chown --linkadd --prepend".split()
