import pytest


class Test(object):

    @pytest.mark.complete("deja-dup -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("deja-dup --help ")
    def test_help(self, completion):
        assert not completion.list
