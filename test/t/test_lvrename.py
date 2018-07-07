import pytest


class TestLvrename(object):

    @pytest.mark.complete("lvrename --",
                          skipif="! lvrename --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
