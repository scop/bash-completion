import pytest


class TestLastlog:
    @pytest.mark.complete("lastlog -")
    def test_1(self, completion):
        assert completion
