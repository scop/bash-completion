import pytest


@pytest.mark.command("btdownloadheadless.py")
class Test(object):

    @pytest.mark.complete("btdownloadheadless.py ")
    def test_(self, completion):
        assert completion.list
