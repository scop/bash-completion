import pytest


@pytest.mark.command("btdownloadcurses.py")
class Test(object):

    @pytest.mark.complete("btdownloadcurses.py ")
    def test_(self, completion):
        assert completion.list
