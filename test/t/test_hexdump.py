import pytest


class TestHexdump(object):

    @pytest.mark.complete("hexdump -")
    def test_1(self, completion):
        assert completion.list
