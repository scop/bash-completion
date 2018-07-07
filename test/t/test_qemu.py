import pytest


class TestQemu(object):

    @pytest.mark.complete("qemu ")
    def test_1(self, completion):
        assert completion.list
