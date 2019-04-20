import pytest


class TestHciattach:
    @pytest.mark.complete("hciattach ")
    def test_1(self, completion):
        assert completion
