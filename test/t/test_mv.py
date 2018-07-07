import pytest


class TestMv(object):

    @pytest.mark.complete("mv ")
    def test_1(self, completion):
        assert completion.list
