import pytest


class TestPr:
    @pytest.mark.complete("pr ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pr -", require_cmd=True)
    def test_options(self, completion):
        assert completion
