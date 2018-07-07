import pytest


class TestChecksec(object):

    @pytest.mark.complete("checksec -")
    def test_1(self, completion):
        assert completion.list
