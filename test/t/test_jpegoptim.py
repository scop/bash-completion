import pytest


class Test(object):

    @pytest.mark.complete("jpegoptim ")
    def test_(self, completion):
        assert completion.list
