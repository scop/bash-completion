import pytest


class TestGetconf(object):

    @pytest.mark.complete("getconf P")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("getconf -")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("getconf -a ")
    def test_3(self, completion):
        assert completion.list

    @pytest.mark.complete("getconf -v ")
    def test_4(self, completion):
        assert completion.list

    @pytest.mark.complete("getconf PATH_MAX ")
    def test_5(self, completion):
        assert completion.list
