import pytest


class TestIp:
    @pytest.mark.complete("ip ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ip a ")
    def test_2(self, completion):
        assert completion
