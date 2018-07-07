import pytest


class TestGcc(object):

    @pytest.mark.complete("gcc ")
    def test_1(self, completion):
        assert completion.list
