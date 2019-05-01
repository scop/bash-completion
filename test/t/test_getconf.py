import pytest


class TestGetconf:
    @pytest.mark.complete("getconf P")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("getconf -")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("getconf -a ")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete(
        "getconf -v ", xfail="! getconf -a 2>&1 | command grep -q ^POSIX_V"
    )
    def test_4(self, completion):
        assert completion

    @pytest.mark.complete("getconf PATH_MAX ")
    def test_5(self, completion):
        assert completion
