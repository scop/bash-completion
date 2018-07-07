import pytest


class TestDu(object):

    @pytest.mark.complete("du ")
    def test_1(self, completion):
        assert completion.list
