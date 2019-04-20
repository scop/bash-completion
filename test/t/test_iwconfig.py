import pytest


class TestIwconfig:
    @pytest.mark.complete("iwconfig --")
    def test_1(self, completion):
        assert completion
