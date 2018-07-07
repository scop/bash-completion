import pytest


class TestWatch(object):

    @pytest.mark.complete("watch -")
    def test_1(self, completion):
        assert completion.list
