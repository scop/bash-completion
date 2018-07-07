import pytest


class TestDot(object):

    @pytest.mark.complete("dot ")
    def test_1(self, completion):
        assert completion.list
