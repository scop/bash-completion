import pytest


class TestIrb(object):

    @pytest.mark.complete("irb ")
    def test_1(self, completion):
        assert completion.list
