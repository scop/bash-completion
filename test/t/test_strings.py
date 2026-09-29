import pytest


class TestStrings:
    @pytest.mark.complete("strings ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("strings -", require_cmd=True)
    def test_2(self, completion):
        assert completion
