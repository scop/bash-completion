import pytest


class TestIscsiadm:
    @pytest.mark.complete("iscsiadm --mod")
    def test_1(self, completion):
        assert completion == "e" or "--mode" in completion
