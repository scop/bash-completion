import pytest


class TestNewusers(object):

    @pytest.mark.complete("newusers ")
    def test_1(self, completion):
        assert completion.list
