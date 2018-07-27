import pytest


class TestTimeout:

    @pytest.mark.complete("timeout ")
    def test_1(self, completion):
        assert not completion.list

    @pytest.mark.complete("timeout -")
    def test_2(self, completion):
        assert completion.list
