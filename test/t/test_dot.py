import pytest


class TestDot:
    @pytest.mark.complete("dot ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("dot t", cwd="dot")
    def test_2(self, completion):
        assert completion == ["test1.gv", "test2.dot"]

    @pytest.mark.complete("dot test1", cwd="dot")
    def test_3(self, completion):
        assert completion == ".gv"
