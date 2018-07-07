import pytest


class TestDir(object):

    @pytest.mark.complete("dir ")
    def test_1(self, completion):
        assert completion.list
