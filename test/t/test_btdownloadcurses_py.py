import pytest


@pytest.mark.bashcomp(cmd="btdownloadcurses.py")
class TestBtdownloadcursesPy:
    @pytest.mark.complete("btdownloadcurses.py ")
    def test_1(self, completion):
        assert completion
