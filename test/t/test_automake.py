import pytest


class TestAutomake(object):

    @pytest.mark.complete("automake ")
    def test_1(self, completion):
        assert completion.list
