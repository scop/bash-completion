import pytest


class TestGenisoimage(object):

    @pytest.mark.complete("genisoimage ")
    def test_1(self, completion):
        assert completion.list
