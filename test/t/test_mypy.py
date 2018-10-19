import pytest


class TestMypy:

    @pytest.mark.complete("mypy ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("mypy --")
    def test_2(self, completion):
        assert completion.list
