import pytest


class TestGmplayer(object):

    @pytest.mark.complete("gmplayer ")
    def test_1(self, completion):
        assert completion.list
