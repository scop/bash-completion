import pytest


class Test(object):

    @pytest.mark.complete("larch library-")
    def test_library(self, completion):
        assert completion.list
