import pytest


class TestOptipng(object):

    @pytest.mark.complete("optipng ")
    def test_1(self, completion):
        assert completion.list
