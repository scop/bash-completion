import pytest


class TestUnrar:
    @pytest.mark.complete("unrar -")
    def test_1(self, completion):
        assert completion
