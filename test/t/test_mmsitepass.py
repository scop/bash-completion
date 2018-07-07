import pytest


class TestMmsitepass(object):

    @pytest.mark.complete("mmsitepass -")
    def test_1(self, completion):
        assert completion.list
