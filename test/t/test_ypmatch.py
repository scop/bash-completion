import pytest


class TestYpmatch:
    # Actually requires ypcat
    @pytest.mark.complete("ypmatch foo ", require_cmd=True)
    def test_1(self, completion):
        assert completion
