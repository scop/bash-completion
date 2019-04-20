import pytest


class TestVgchange:
    @pytest.mark.complete("vgchange -")
    def test_1(self, completion):
        assert completion
