import pytest


class Test(object):

    @pytest.mark.complete("chsh ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("chsh -s ")
    def test_s(self, completion):
        assert completion.list
