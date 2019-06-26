import pytest


class TestOpera:
    @pytest.mark.complete("opera ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("opera -", require_cmd=True)
    def test_2(self, completion):
        assert completion
