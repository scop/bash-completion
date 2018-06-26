import pytest


class Test(object):

    @pytest.mark.complete("xmllint ")
    def test_(self, completion):
        assert completion.list
