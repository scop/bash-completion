import pytest


class TestMussh:
    @pytest.mark.complete("mussh -", require_cmd=True)
    def test_1(self, completion):
        assert completion
