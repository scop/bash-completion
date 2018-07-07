import pytest


class TestRoute(object):

    @pytest.mark.complete("route ")
    def test_1(self, completion):
        assert completion.list
