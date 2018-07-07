import pytest


class TestId(object):

    @pytest.mark.complete("id -")
    def test_1(self, completion):
        assert completion.list
