import pytest


class TestSet(object):

    @pytest.mark.complete("set no")
    def test_1(self, completion):
        assert completion.list
