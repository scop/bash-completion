import pytest


class TestSh:
    @pytest.mark.complete("sh -")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("sh +")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("sh -o ")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("sh -c ")
    def test_4(self, completion):
        assert not completion
