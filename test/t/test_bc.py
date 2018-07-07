import pytest


class TestBc(object):

    @pytest.mark.complete("bc --")
    def test_1(self, completion):
        assert completion.list
