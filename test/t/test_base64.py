import pytest


class Test(object):

    @pytest.mark.complete("base64 ")
    def test_(self, completion):
        assert completion.list
