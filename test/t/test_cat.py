import pytest


class TestCat(object):

    @pytest.mark.complete("cat ")
    def test_1(self, completion):
        assert completion.list
