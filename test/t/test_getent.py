import pytest


class TestGetent(object):

    @pytest.mark.complete("getent ")
    def test_1(self, completion):
        assert completion.list
