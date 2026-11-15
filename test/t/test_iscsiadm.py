import pytest


class TestIscsiadm:
    @pytest.mark.complete("iscsiadm --mod")
    def test_1(self, completion):
        assert completion == "e" or "--mode" in completion

    @pytest.mark.complete("iscsiadm --mode nonexistent-mode --")
    def test_unknown_mode(self, completion):
        assert not completion
