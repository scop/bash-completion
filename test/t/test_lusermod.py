import pytest


class TestLusermod:
    @pytest.mark.complete("lusermod ")
    def test_1(self, completion):
        assert completion
