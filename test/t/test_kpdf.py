import pytest


class TestKpdf(object):

    @pytest.mark.complete("kpdf ", cwd="kpdf")
    def test_1(self, completion):
        assert completion.list == "foo/ .eps .ps .EPS .PS .pdf .PDF".split()
