import pytest


class TestMonodevelop(object):

    @pytest.mark.complete("monodevelop ")
    def test_1(self, completion):
        assert completion.list
