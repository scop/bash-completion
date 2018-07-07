import pytest


class TestRlog(object):

    @pytest.mark.complete("rlog ")
    def test_1(self, completion):
        assert completion.list
