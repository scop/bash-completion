import pytest


class TestFilesnarf:
    @pytest.mark.complete("filesnarf -", require_cmd=True)
    def test_1(self, completion):
        assert completion
