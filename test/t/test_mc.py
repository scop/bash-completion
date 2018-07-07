import pytest


class TestMc(object):

    @pytest.mark.complete("mc -")
    def test_1(self, completion):
        assert completion.list
