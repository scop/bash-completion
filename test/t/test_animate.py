import pytest


class TestAnimate(object):

    @pytest.mark.complete("animate ")
    def test_1(self, completion):
        assert completion.list
