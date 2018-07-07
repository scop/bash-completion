import pytest


class TestTouch(object):

    @pytest.mark.complete("touch --",
                          skipif="! touch --help &>/dev/null")
    def test_1(self, completion):
        assert completion.list
