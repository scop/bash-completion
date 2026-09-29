import pytest


class TestHciconfig:
    @pytest.mark.complete("hciconfig ")
    def test_1(self, completion):
        assert completion
