import pytest


class TestIrb:
    @pytest.mark.complete("irb ")
    def test_1(self, completion):
        assert completion
