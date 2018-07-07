import pytest


class TestLvscan(object):

    @pytest.mark.complete("lvscan --",
                          skipif="! lvscan --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
