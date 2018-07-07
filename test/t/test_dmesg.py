import pytest


class TestDmesg(object):

    @pytest.mark.complete("dmesg -")
    def test_1(self, completion):
        assert completion.list
