import pytest


class TestIwlist:
    @pytest.mark.complete("iwlist --")
    def test_1(self, completion):
        assert completion
