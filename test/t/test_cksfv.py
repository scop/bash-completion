import pytest


class TestCksfv(object):

    @pytest.mark.complete("cksfv -")
    def test_1(self, completion):
        assert completion.list
