import pytest


class TestSshmitm(object):

    @pytest.mark.complete("sshmitm -")
    def test_1(self, completion):
        assert completion.list
