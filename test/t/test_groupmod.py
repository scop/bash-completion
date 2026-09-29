import pytest


class TestGroupmod:
    @pytest.mark.complete("groupmod ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("groupmod -", require_cmd=True)
    def test_2(self, completion):
        assert completion
