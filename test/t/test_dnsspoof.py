import pytest


class TestDnsspoof:
    @pytest.mark.complete("dnsspoof -", require_cmd=True)
    def test_1(self, completion):
        assert completion
