import pytest


class TestUscan(object):

    @pytest.mark.complete("uscan -")
    def test_1(self, completion):
        assert completion.list
