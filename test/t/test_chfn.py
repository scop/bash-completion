import pytest


class TestChfn(object):

    @pytest.mark.complete("chfn ")
    def test_1(self, completion):
        assert completion.list
