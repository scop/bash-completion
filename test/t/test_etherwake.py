import pytest


class TestEtherwake:
    @pytest.mark.complete("etherwake -")
    def test_1(self, completion):
        assert completion
