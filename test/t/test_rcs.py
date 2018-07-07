import pytest


class TestRcs(object):

    @pytest.mark.complete("rcs ")
    def test_1(self, completion):
        assert completion.list
