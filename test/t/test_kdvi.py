import pytest


class TestKdvi:
    @pytest.mark.complete("kdvi ", cwd="kdvi")
    def test_1(self, completion):
        assert completion == sorted(
            "foo/ .dvi .DVI .dvi.bz2 .DVI.bz2 .dvi.gz "
            ".DVI.gz .dvi.Z .DVI.Z".split()
        )
