import pytest


class TestIdentify:
    @pytest.mark.complete("identify -")
    def test_1(self, completion):
        assert completion
