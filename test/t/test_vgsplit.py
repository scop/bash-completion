import pytest


class TestVgsplit(object):

    @pytest.mark.complete("vgsplit -")
    def test_1(self, completion):
        assert completion.list
