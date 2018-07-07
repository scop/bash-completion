import pytest


class TestXmllint(object):

    @pytest.mark.complete("xmllint ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("xmllint -")
    def test_2(self, completion):
        assert completion.list
