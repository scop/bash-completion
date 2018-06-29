import pytest


class Test(object):

    @pytest.mark.complete("sdptool ")
    def test_(self, completion):
        assert completion.list
