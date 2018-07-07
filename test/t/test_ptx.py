import pytest


class TestPtx(object):

    @pytest.mark.complete("ptx ")
    def test_1(self, completion):
        assert completion.list
