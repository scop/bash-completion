import pytest


class Test(object):

    @pytest.mark.complete("set no")
    def test_no(self, completion):
        assert completion.list
