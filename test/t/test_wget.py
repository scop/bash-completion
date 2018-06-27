import pytest


class Test(object):

    @pytest.mark.complete("wget ")
    def test_(self, completion):
        assert not completion.list

    @pytest.mark.complete("wget --h")
    def test_h(self, completion):
        assert completion.list
