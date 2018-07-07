import pytest


class TestCal(object):

    @pytest.mark.complete("cal ")
    def test_1(self, completion):
        assert completion.list
