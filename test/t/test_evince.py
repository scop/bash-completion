import pytest

from conftest import assert_complete, create_dummy_filedirs


@pytest.mark.bashcomp(temp_cwd=True)
class TestEvince:
    def test_1(self, bash):
        files, dirs = create_dummy_filedirs(
            (
                ".cb7 .CB7 .cbr .CBR .cbt .CBT .cbz .CBZ .djv .DJV .djvu "
                ".DJVU .dvi .DVI .dvi.bz2 .dvi.BZ2 .DVI.bz2 .DVI.BZ2 .dvi.gz "
                ".dvi.GZ .DVI.gz .DVI.GZ .eps .EPS .eps.bz2 .eps.BZ2 .EPS.bz2 "
                ".EPS.BZ2 .eps.gz .eps.GZ .EPS.gz .EPS.GZ .oxps .OXPS .pdf "
                ".PDF .pdf.bz2 .pdf.BZ2 .PDF.bz2 .PDF.BZ2 .pdf.gz .pdf.GZ "
                ".PDF.gz .PDF.GZ .ps .PS .ps.bz2 .ps.BZ2 .PS.bz2 .PS.BZ2 "
                ".ps.gz .ps.GZ .PS.gz .PS.GZ .tif .TIF .tiff .TIFF .txt .TXT "
                ".xps .XPS"
            ).split(),
            "foo".split(),
        )

        completion = assert_complete(bash, "evince ")
        assert completion == [
            x
            for x in sorted(files + ["%s/" % d for d in dirs])
            if x.lower() != ".txt"
        ]

    @pytest.mark.complete("evince -", require_cmd=True)
    def test_2(self, completion):
        assert completion
