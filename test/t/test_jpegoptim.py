import pytest


class TestJpegoptim:

    @pytest.mark.complete("jpegoptim ")
    def test_1(self, completion):
        assert completion
