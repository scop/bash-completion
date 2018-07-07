import pytest


class TestRmlist(object):

    @pytest.mark.complete("rmlist -")
    def test_1(self, completion):
        assert completion.list
