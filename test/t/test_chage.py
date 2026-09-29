import pytest


class TestChage:
    @pytest.mark.complete("chage ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("chage -", require_cmd=True)
    def test_2(self, completion):
        assert completion
