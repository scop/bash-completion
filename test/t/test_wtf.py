import pytest


class TestWtf(object):

    @pytest.mark.complete("wtf A")
    def test_1(self, completion):
        assert completion.list
