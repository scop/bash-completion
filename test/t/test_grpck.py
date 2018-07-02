import pytest


class Test(object):

    @pytest.mark.complete("grpck ")
    def test_(self, completion):
        assert completion.list
