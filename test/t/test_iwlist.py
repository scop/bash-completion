import pytest


class TestIwlist(object):

    @pytest.mark.complete("iwlist --")
    def test_1(self, completion):
        assert completion.list
