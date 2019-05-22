import pytest


class TestInterdiff:
    @pytest.mark.complete("interdiff ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("interdiff -")
    def test_2(self, completion):
        assert completion
