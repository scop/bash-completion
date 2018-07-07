import pytest


class TestLilo(object):

    @pytest.mark.complete("lilo -")
    def test_1(self, completion):
        assert completion.list
