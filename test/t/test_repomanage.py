import pytest


class TestRepomanage(object):

    @pytest.mark.complete("repomanage ")
    def test_1(self, completion):
        assert completion.list
