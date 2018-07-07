import pytest


class TestBind(object):

    @pytest.mark.complete("bind -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("bind k")
    def test_2(self, completion):
        assert completion.list
