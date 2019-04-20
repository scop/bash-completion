import pytest


class TestKpdf:
    @pytest.mark.complete("kpdf ", cwd="kpdf")
    def test_1(self, completion):
        assert completion == "foo/ .eps .ps .EPS .PS .pdf .PDF".split()
