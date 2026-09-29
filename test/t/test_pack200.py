import pytest


class TestPack200:
    @pytest.mark.complete("pack200 ")
    def test_1(self, completion):
        assert completion
