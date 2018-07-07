import pytest


class TestMsynctool(object):

    @pytest.mark.complete("msynctool ")
    def test_1(self, completion):
        assert completion.list
