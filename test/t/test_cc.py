import pytest


class TestCc:
    @pytest.mark.complete("cc ")
    def test_1(self, completion):
        assert completion
