import pytest


class TestLuserdel(object):

    @pytest.mark.complete("luserdel ")
    def test_1(self, completion):
        assert completion.list
