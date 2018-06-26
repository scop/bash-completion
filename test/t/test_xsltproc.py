import pytest


class Test(object):

    @pytest.mark.complete("xsltproc ")
    def test_(self, completion):
        assert completion.list
