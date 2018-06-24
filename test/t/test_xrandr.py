import pytest


class Test(object):

    @pytest.mark.complete("xrandr ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("xrandr --mode ")
    def test_mode(self, completion):
        assert not completion.list
