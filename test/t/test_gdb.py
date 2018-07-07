import pytest


class TestGdb(object):

    @pytest.mark.complete("gdb - ")
    def test_1(self, completion):
        assert completion.list
