import pytest


class TestDict:
    @pytest.mark.complete("dict -", require_cmd=True)
    def test_1(self, completion):
        assert completion
