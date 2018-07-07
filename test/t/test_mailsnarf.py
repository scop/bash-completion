import pytest


class TestMailsnarf(object):

    @pytest.mark.complete("mailsnarf -")
    def test_1(self, completion):
        assert completion.list
