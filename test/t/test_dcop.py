import pytest


class TestDcop:
    @pytest.mark.complete("dcop ", require_cmd=True)
    def test_1(self, completion):
        assert completion
