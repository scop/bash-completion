import pytest


class TestNm(object):

    @pytest.mark.complete("nm ")
    def test_1(self, completion):
        assert completion.list
