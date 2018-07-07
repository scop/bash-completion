import pytest


class TestSnownews(object):

    @pytest.mark.complete("snownews --")
    def test_1(self, completion):
        assert completion.list
