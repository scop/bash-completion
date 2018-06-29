import pytest


class Test(object):

    @pytest.mark.complete("stream ")
    def test_(self, completion):
        assert completion.list
