import pytest


class TestSplit(object):

    @pytest.mark.complete("split --",
                          skipif="! split --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
