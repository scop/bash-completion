import pytest


class TestJpegoptim(object):

    @pytest.mark.complete("jpegoptim ")
    def test_1(self, completion):
        assert completion.list
