import pytest


class TestSeq(object):

    @pytest.mark.complete("seq --")
    def test_1(self, completion):
        assert completion.list
