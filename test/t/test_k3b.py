import pytest


class TestK3b:
    @pytest.mark.complete("k3b ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("k3b -", require_cmd=True)
    def test_2(self, completion):
        assert completion
