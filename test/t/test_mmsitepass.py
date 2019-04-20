import pytest


class TestMmsitepass:
    @pytest.mark.complete("mmsitepass -")
    def test_1(self, completion):
        assert completion
