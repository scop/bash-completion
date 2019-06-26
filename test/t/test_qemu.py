import pytest


class TestQemu:
    @pytest.mark.complete("qemu ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("qemu -", require_cmd=True)
    def test_2(self, completion):
        assert completion
