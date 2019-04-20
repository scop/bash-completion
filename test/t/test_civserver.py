import pytest


class TestCivserver:
    @pytest.mark.complete("civserver -")
    def test_1(self, completion):
        assert completion
