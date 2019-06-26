import pytest


class TestEog:
    @pytest.mark.complete("eog ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("eog -", require_cmd=True)
    def test_2(self, completion):
        assert completion
