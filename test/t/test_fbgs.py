import pytest


class TestFbgs(object):

    @pytest.mark.complete("fbgs ")
    def test_1(self, completion):
        assert completion.list
