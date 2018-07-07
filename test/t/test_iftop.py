import pytest


class TestIftop(object):

    @pytest.mark.complete("iftop ")
    def test_1(self, completion):
        assert completion.list
