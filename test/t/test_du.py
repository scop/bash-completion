import pytest


class TestDu:
    @pytest.mark.complete("du ")
    def test_1(self, completion):
        assert completion
