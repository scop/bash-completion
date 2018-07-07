import pytest


class TestWithlist(object):

    @pytest.mark.complete("withlist --")
    def test_1(self, completion):
        assert completion.list
