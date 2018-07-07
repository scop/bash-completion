import pytest


class TestNethogs(object):

    @pytest.mark.complete("nethogs ")
    def test_1(self, completion):
        assert completion.list
