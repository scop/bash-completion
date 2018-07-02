import pytest


class Test(object):

    @pytest.mark.complete("md5sum ")
    def test_(self, completion):
        assert completion.list
