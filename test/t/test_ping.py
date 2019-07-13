import pytest


class TestPing:
    @pytest.mark.complete("ping ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("ping -", require_cmd=True)
    def test_2(self, completion):
        assert completion
