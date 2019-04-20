import pytest


class TestDnsspoof:
    @pytest.mark.complete("dnsspoof -")
    def test_1(self, completion):
        assert completion
