import pytest


@pytest.mark.command("btdownloadheadless.py")
class TestBtdownloadheadlessPy(object):

    @pytest.mark.complete("btdownloadheadless.py ")
    def test_1(self, completion):
        assert completion.list
