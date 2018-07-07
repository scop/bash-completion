import pytest


class TestFbi(object):

    @pytest.mark.complete("fbi ")
    def test_1(self, completion):
        assert completion.list
