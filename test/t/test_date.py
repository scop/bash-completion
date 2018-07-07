import pytest


class TestDate(object):

    @pytest.mark.complete("date ")
    def test_1(self, completion):
        assert completion.list
