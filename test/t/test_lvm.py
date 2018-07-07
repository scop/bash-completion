import pytest


class TestLvm(object):

    @pytest.mark.complete("lvm pv")
    def test_1(self, completion):
        assert completion.list
