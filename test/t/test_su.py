import pytest


class TestSu(object):

    @pytest.mark.complete("su ")
    def test_1(self, completion):
        assert completion.list
