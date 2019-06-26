import pytest


class TestEvince:
    @pytest.mark.complete("evince ", cwd="evince")
    def test_1(self, completion):
        # .txt should not be here
        assert completion == sorted(
            "foo/ .bmp .BMP .cbr .CBR .cbz .CBZ .djv .DJV .djvu .DJVU .dvi "
            ".DVI .dvi.bz2 .dvi.BZ2 .DVI.bz2 .DVI.BZ2 .dvi.gz .dvi.GZ "
            ".DVI.gz .DVI.GZ .eps .EPS .eps.bz2 .eps.BZ2 .EPS.bz2 .EPS.BZ2 "
            ".eps.gz .eps.GZ .EPS.gz .EPS.GZ .gif .GIF .ico .ICO .jpeg "
            ".JPEG .jpg .JPG .miff .MIFF .pbm .PBM .pcx .PCX .pdf .PDF "
            ".pdf.bz2 .pdf.BZ2 .PDF.bz2 .PDF.BZ2 .pdf.gz .pdf.GZ .PDF.gz "
            ".PDF.GZ .pgm .PGM .png .PNG .pnm .PNM .ppm .PPM .ps .PS "
            ".ps.bz2 .ps.BZ2 .PS.bz2 .PS.BZ2 .ps.gz .ps.GZ .PS.gz .PS.GZ "
            ".tga .TGA .tif .TIF .tiff .TIFF .xpm .XPM .xwd .XWD".split()
        )

    @pytest.mark.complete("evince -", require_cmd=True)
    def test_2(self, completion):
        assert completion
