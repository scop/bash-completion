import pytest


class TestMsgsnarf(object):

    @pytest.mark.complete("msgsnarf -")
    def test_1(self, completion):
        assert completion.list
