import pytest


class TestGrub:
    @pytest.mark.complete("grub --")
    def test_1(self, completion):
        assert completion
