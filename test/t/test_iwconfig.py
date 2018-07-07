import pytest


class TestIwconfig(object):

    @pytest.mark.complete("iwconfig --")
    def test_1(self, completion):
        assert completion.list
