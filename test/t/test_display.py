import pytest


class TestDisplay:

    @pytest.mark.complete("display ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("display -")
    def test_2(self, completion):
        assert completion.list
