import pytest


class TestPovray(object):

    @pytest.mark.complete("povray ")
    def test_1(self, completion):
        assert completion.list
