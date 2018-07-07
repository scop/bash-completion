import pytest


class TestDsniff(object):

    @pytest.mark.complete("dsniff -")
    def test_1(self, completion):
        assert completion.list
