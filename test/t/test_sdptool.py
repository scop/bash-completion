import pytest


class TestSdptool:
    @pytest.mark.complete("sdptool ")
    def test_1(self, completion):
        assert completion
