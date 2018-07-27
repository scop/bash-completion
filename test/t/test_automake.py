import pytest


class TestAutomake:

    @pytest.mark.complete("automake ")
    def test_1(self, completion):
        assert completion.list
