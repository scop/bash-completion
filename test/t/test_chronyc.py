import pytest


class TestChronyc:
    @pytest.mark.complete("chronyc ", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("chronyc -", require_cmd=True)
    def test_2(self, completion):
        assert completion
