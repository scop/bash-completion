import pytest


class TestNl:
    @pytest.mark.complete("nl ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("nl -", require_cmd=True)
    def test_options(self, completion):
        assert completion
