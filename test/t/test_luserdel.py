import pytest


class TestLuserdel:
    @pytest.mark.complete("luserdel ")
    def test_1(self, completion):
        assert completion
