import pytest


class TestMtr:
    @pytest.mark.complete("mtr ")
    def test_basic(self, completion):
        assert completion
