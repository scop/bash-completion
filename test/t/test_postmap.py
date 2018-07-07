import pytest


class TestPostmap(object):

    @pytest.mark.complete("postmap ")
    def test_1(self, completion):
        assert completion.list
