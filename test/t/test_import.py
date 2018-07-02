import pytest


class Test(object):

    @pytest.mark.complete("import ")
    def test_(self, completion):
        assert completion.list
