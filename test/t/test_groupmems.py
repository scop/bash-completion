import pytest


class TestGroupmems:
    @pytest.mark.complete("groupmems -")
    def test_1(self, completion):
        assert completion
