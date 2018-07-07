import pytest


class TestLdapsearch(object):

    @pytest.mark.complete("ldapsearch -")
    def test_1(self, completion):
        assert completion.list
