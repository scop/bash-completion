import pytest


class TestE2freefrag(object):

    @pytest.mark.complete("e2freefrag ")
    def test_1(self, completion):
        assert completion.list
