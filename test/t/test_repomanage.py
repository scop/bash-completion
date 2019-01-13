import pytest


class TestRepomanage:

    @pytest.mark.complete("repomanage ")
    def test_1(self, completion):
        assert completion
