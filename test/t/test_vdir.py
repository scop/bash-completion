import pytest


class TestVdir:
    @pytest.mark.complete("vdir ")
    def test_1(self, completion):
        assert completion
