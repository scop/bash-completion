import pytest


class TestKldload(object):

    @pytest.mark.complete("kldload ")
    def test_1(self, completion):
        assert completion.list
