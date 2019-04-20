import pytest


class TestIdn:
    @pytest.mark.complete("idn -")
    def test_1(self, completion):
        assert completion
