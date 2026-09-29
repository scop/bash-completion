import pytest


class TestIonice:
    @pytest.mark.complete("ionice -", require_cmd=True)
    def test_1(self, completion):
        assert completion
