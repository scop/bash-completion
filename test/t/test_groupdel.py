import pytest


class TestGroupdel:
    @pytest.mark.complete("groupdel ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("groupdel -")
    def test_2(self, completion):
        assert completion
