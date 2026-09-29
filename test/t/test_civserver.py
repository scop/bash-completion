import pytest


class TestCivserver:
    @pytest.mark.complete("civserver -", require_cmd=True)
    def test_1(self, completion):
        assert completion
