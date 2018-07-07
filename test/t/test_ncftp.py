import pytest


class TestNcftp(object):

    @pytest.mark.complete("ncftp ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("ncftp -")
    def test_2(self, completion):
        assert completion.list
