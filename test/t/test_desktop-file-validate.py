import pytest


class Test(object):

    @pytest.mark.complete("desktop-file-validate ")
    def test_(self, completion):
        assert completion.list
