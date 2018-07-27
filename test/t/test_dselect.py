import pytest


class TestDselect:

    @pytest.mark.complete("dselect ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("dselect -")
    def test_2(self, completion):
        assert completion.list
