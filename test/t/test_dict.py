import pytest


class TestDict(object):

    @pytest.mark.complete("dict -")
    def test_1(self, completion):
        assert completion.list
