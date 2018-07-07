import pytest


class TestGrep(object):

    @pytest.mark.complete("grep --")
    def test_1(self, completion):
        assert completion.list
