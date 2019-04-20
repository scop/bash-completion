import pytest


class TestPkgtool:
    @pytest.mark.complete("pkgtool -")
    def test_1(self, completion):
        assert completion
