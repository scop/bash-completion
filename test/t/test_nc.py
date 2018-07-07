import pytest


class TestNc(object):

    @pytest.mark.complete("nc -")
    def test_1(self, completion):
        assert completion.list
