import pytest


class TestVmstat(object):

    @pytest.mark.complete("vmstat -")
    def test_1(self, completion):
        assert completion.list
