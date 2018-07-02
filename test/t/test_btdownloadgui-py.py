import pytest


@pytest.mark.command("btdownloadgui.py")
class Test(object):

    @pytest.mark.complete("btdownloadgui.py ")
    def test_(self, completion):
        assert completion.list
