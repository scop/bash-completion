import pytest


class TestAclocal:
    @pytest.mark.complete("aclocal ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("aclocal -", require_cmd=True)
    def test_2(self, completion):
        assert completion
