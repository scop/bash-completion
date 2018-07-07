import pytest


class TestKtutil(object):

    @pytest.mark.complete("ktutil ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("ktutil -")
    def test_2(self, completion):
        assert completion.list
