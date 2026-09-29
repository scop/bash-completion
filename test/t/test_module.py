import pytest


class TestModule:
    @pytest.mark.complete("module ")
    def test_1(self, completion):
        assert completion
