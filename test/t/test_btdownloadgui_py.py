import pytest


@pytest.mark.bashcomp(
    cmd="btdownloadgui.py",
)
class TestBtdownloadguiPy(object):

    @pytest.mark.complete("btdownloadgui.py ")
    def test_1(self, completion):
        assert completion.list
