import pytest


class TestVgsplit:
    @pytest.mark.complete("vgsplit -")
    def test_1(self, completion):
        assert completion
