import pytest


class TestZopflipng(object):

    @pytest.mark.complete("zopflipng ")
    def test_1(self, completion):
        assert completion.list
