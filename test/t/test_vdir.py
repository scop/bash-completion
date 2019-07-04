import pytest


class TestVdir:
    @pytest.mark.complete("vdir ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("vdir -", require_cmd=True)
    def test_options(self, completion):
        assert completion
