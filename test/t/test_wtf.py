import pytest


class Test(object):

    @pytest.mark.complete("wtf A")
    def test_A(self, completion):
        assert completion.list
