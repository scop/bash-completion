import pytest


class TestTac:

    @pytest.mark.complete("tac --")
    def test_1(self, completion):
        assert completion
