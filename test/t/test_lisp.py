import pytest


class TestLisp(object):

    @pytest.mark.complete("lisp ")
    def test_1(self, completion):
        assert completion.list
