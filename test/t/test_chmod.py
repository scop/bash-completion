import pytest


class Test(object):

    # No completion here until mode completion is implemented
    @pytest.mark.complete("chmod ")
    def test_(self, completion):
        assert not completion.list

    @pytest.mark.complete("chmod 755 ")
    def test_755(self, completion):
        assert completion.list

    @pytest.mark.complete("chmod -")
    def test_dash(self, completion):
        assert completion.list
