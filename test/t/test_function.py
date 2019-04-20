import pytest


class TestFunction:
    @pytest.mark.complete("function _parse_")
    def test_1(self, completion):
        assert completion
