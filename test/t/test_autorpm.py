import pytest


class TestAutorpm:
    @pytest.mark.complete("autorpm ")
    def test_1(self, completion):
        assert completion
