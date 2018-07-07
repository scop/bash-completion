import pytest


class TestExpand(object):

    @pytest.mark.complete("expand --",
                          skipif="! expand --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
