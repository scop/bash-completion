import pytest


class Test(object):

    @pytest.mark.complete("ccze ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("ccze -? ")
    def test_questionmark(self, completion):
        assert not completion.list

    @pytest.mark.complete("ccze -o ")
    def test_o(self, completion):
        assert completion.list

    @pytest.mark.complete("ccze --plugin=")
    def test_plugin(self, completion):
        assert completion.list
