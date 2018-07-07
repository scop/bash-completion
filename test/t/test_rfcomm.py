import pytest


class TestRfcomm(object):

    @pytest.mark.complete("rfcomm ")
    def test_1(self, completion):
        assert completion.list
