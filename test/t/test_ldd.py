import pytest


class TestLdd:
    @pytest.mark.complete("ldd ")
    def test_1(self, completion):
        assert completion
