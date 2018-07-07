import pytest


class TestDiff(object):

    @pytest.mark.complete("diff --")
    def test_1(self, completion):
        assert completion.list
