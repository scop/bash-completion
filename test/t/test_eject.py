import pytest


class TestEject:
    @pytest.mark.complete("eject -")
    def test_1(self, completion):
        assert completion
