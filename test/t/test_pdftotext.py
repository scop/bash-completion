import pytest


class Test(object):

    @pytest.mark.complete("pdftotext ")
    def test_(self, completion):
        assert completion.list
