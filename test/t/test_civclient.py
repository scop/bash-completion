import pytest


class TestCivclient(object):

    @pytest.mark.complete("civclient -")
    def test_1(self, completion):
        assert completion.list
