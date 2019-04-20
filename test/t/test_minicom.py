import pytest


class TestMinicom:
    @pytest.mark.complete("minicom -")
    def test_1(self, completion):
        assert completion
