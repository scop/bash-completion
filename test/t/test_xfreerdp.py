import pytest


class TestXfreerdp:

    @pytest.mark.complete("xfreerdp /")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("xfreerdp -")
    def test_2(self, completion):
        assert completion

    @pytest.mark.complete("xfreerdp +")
    def test_3(self, completion):
        assert completion

    @pytest.mark.complete("xfreerdp /kbd:")
    def test_4(self, completion):
        assert completion

    @pytest.mark.complete("xfreerdp /help ")
    def test_5(self, completion):
        assert not completion
