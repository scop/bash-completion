import pytest


class TestAutoheader:
    @pytest.mark.complete("autoheader ")
    def test_1(self, completion):
        assert completion
