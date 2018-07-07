import pytest


class TestLastlog(object):

    @pytest.mark.complete("lastlog -")
    def test_1(self, completion):
        assert completion.list
