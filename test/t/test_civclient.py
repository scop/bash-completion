import pytest


class TestCivclient:
    @pytest.mark.complete("civclient -")
    def test_1(self, completion):
        assert completion
