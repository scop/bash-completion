import pytest


class TestMtx(object):

    @pytest.mark.complete("mtx ")
    def test_1(self, completion):
        assert completion.list
