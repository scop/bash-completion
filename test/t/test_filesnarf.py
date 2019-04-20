import pytest


class TestFilesnarf:
    @pytest.mark.complete("filesnarf -")
    def test_1(self, completion):
        assert completion
