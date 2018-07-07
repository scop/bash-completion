import pytest


class TestQuota(object):

    @pytest.mark.complete("quota ")
    def test_1(self, completion):
        assert completion.list
