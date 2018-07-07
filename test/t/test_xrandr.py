import pytest


class TestXrandr(object):

    @pytest.mark.complete("xrandr ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("xrandr --mode ")
    def test_2(self, completion):
        assert not completion.list
