import pytest


class TestJpegoptim:
    @pytest.mark.complete("jpegoptim ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("jpegoptim -")
    def test_2(self, completion):
        assert completion
