import pytest


class TestDselect:
    @pytest.mark.complete("dselect ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("dselect -", require_cmd=True)
    def test_2(self, completion):
        assert completion
