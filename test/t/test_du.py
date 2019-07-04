import pytest


class TestDu:
    @pytest.mark.complete("du ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("du -", require_cmd=True)
    def test_options(self, completion):
        assert completion
