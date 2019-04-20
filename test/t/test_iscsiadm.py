import pytest


class TestIscsiadm:
    @pytest.mark.complete("iscsiadm --mode")
    def test_1(self, completion):
        assert completion
