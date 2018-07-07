import pytest


class TestHddtemp(object):

    @pytest.mark.complete("hddtemp -")
    def test_1(self, completion):
        assert completion.list
