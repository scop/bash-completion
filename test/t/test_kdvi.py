import pytest


class TestKdvi(object):

    @pytest.mark.complete("kdvi ", cwd="kdvi")
    def test_1(self, completion):
        assert completion.list == "foo/ .dvi .DVI .dvi.bz2 .DVI.bz2 .dvi.gz " \
            ".DVI.gz .dvi.Z .DVI.Z".split()
