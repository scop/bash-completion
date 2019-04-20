import pytest


class TestMedusa:
    @pytest.mark.complete("medusa -")
    def test_1(self, completion):
        assert completion
