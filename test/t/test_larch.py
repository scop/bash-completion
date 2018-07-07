import pytest


class TestLarch(object):

    @pytest.mark.complete("larch library-")
    def test_1(self, completion):
        assert completion.list
