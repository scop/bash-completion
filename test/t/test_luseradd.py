import pytest


class TestLuseradd:
    @pytest.mark.complete("luseradd -")
    def test_1(self, completion):
        assert completion
