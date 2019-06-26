import pytest


class TestPine:
    @pytest.mark.complete("pine -", require_cmd=True)
    def test_1(self, completion):
        assert completion
