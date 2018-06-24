import pytest


class Test(object):

    @pytest.mark.complete("xxd ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("xxd -")
    def test_dash(self, completion):
        assert completion.list
