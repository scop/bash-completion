import pytest


class TestSort(object):

    @pytest.mark.complete("sort --")
    def test_1(self, completion):
        assert completion.list
