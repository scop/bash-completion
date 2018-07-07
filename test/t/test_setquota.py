import pytest


class TestSetquota(object):

    @pytest.mark.complete("setquota ")
    def test_1(self, completion):
        assert completion.list
