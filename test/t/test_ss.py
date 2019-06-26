import pytest


class TestSs:
    @pytest.mark.complete("ss -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ss -A ", require_cmd=True)
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("ss -A foo,", require_cmd=True)
    def test_3(self, completion):
        assert completion
