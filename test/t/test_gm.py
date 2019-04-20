import pytest


class TestGm:
    @pytest.mark.complete("gm ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("gm help ")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("gm time ")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("gm version ")
    def test_4(self, completion):
        assert not completion
