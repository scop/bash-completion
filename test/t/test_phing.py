import pytest


class TestPhing:
    @pytest.mark.complete("phing -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("phing -l ", require_cmd=True)
    def test_2(self, completion):
        assert not completion
