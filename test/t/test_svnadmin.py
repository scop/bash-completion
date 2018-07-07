import pytest


class TestSvnadmin(object):

    @pytest.mark.complete("svnadmin ")
    def test_1(self, completion):
        assert completion.list
