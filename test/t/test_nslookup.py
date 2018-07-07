import pytest


class TestNslookup(object):

    @pytest.mark.complete("nslookup -")
    def test_1(self, completion):
        assert completion.list
