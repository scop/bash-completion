import pytest


class TestTipc:
    @pytest.mark.complete("tipc ")
    def test_1(self, completion):
        assert completion
