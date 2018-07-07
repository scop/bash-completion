import pytest


class TestComplete(object):

    @pytest.mark.complete("complete -")
    def test_1(self, completion):
        assert completion.list
