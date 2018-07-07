import pytest


class TestPkill(object):

    @pytest.mark.complete("pkill ")
    def test_1(self, completion):
        assert completion.list
