import pytest


class TestWebmitm(object):

    @pytest.mark.complete("webmitm -")
    def test_1(self, completion):
        assert completion.list
