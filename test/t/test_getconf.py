import pytest


class Test(object):

    @pytest.mark.complete("getconf P")
    def test_p(self, completion):
        assert completion.list

    @pytest.mark.complete("getconf -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("getconf -a ")
    def test_a(self, completion):
        assert completion.list

    @pytest.mark.complete("getconf -v ")
    def test_v(self, completion):
        assert completion.list

    @pytest.mark.complete("getconf PATH_MAX ")
    def test_path_max(self, completion):
        assert completion.list
