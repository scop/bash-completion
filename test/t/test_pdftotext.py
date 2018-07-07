import pytest


class TestPdftotext(object):

    @pytest.mark.complete("pdftotext ")
    def test_1(self, completion):
        assert completion.list
