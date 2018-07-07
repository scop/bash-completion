import pytest


class TestDfutool(object):

    @pytest.mark.complete("dfutool ")
    def test_1(self, completion):
        assert completion.list
