import pytest


class TestGrub:
    @pytest.mark.complete("grub --", require_cmd=True)
    def test_1(self, completion):
        assert completion
