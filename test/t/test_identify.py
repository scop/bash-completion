import pytest


class TestIdentify:
    @pytest.mark.complete("identify -", require_cmd=True)
    def test_1(self, completion):
        assert completion
