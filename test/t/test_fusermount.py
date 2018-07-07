import pytest


class TestFusermount(object):

    @pytest.mark.complete("fusermount ")
    def test_1(self, completion):
        assert completion.list
