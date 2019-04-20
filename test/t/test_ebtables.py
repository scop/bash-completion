import pytest


class TestEbtables:
    @pytest.mark.complete("ebtables -")
    def test_1(self, completion):
        assert completion
