import pytest


class TestRdict(object):

    @pytest.mark.complete("rdict --")
    def test_1(self, completion):
        assert completion.list
