import pytest


class TestConjure(object):

    @pytest.mark.complete("conjure ")
    def test_1(self, completion):
        assert completion.list
