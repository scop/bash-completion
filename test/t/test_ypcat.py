import pytest


class TestYpcat:
    @pytest.mark.complete("ypcat ", require_cmd=True)
    def test_1(self, completion):
        assert completion
