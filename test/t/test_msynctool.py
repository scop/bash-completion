import pytest


class TestMsynctool:
    @pytest.mark.complete("msynctool ")
    def test_1(self, completion):
        assert completion
