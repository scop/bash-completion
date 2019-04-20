import pytest


class TestIwpriv:
    @pytest.mark.complete("iwpriv --")
    def test_1(self, completion):
        assert completion
