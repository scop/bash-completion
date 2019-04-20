import pytest


class TestRpcdebug:
    @pytest.mark.complete("rpcdebug -")
    def test_1(self, completion):
        assert completion
