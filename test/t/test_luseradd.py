import pytest


class TestLuseradd:
    @pytest.mark.complete("luseradd -", require_cmd=True)
    def test_1(self, completion):
        assert completion
