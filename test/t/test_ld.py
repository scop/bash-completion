import pytest


class TestLd(object):

    @pytest.mark.complete("ld ")
    def test_1(self, completion):
        assert completion.list
