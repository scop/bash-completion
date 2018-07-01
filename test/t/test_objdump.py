import pytest


class Test(object):

    @pytest.mark.complete("objdump ")
    def test_(self, completion):
        assert completion.list
