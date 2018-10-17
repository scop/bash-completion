import pytest


class TestOp:

    @pytest.mark.complete("op ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("op --")
    def test_2(self, completion):
        assert completion.list
