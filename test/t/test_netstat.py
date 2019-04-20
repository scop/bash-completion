import pytest


class TestNetstat:
    @pytest.mark.complete("netstat ")
    def test_1(self, completion):
        assert completion
