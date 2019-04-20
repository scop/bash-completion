import pytest


@pytest.mark.bashcomp(cmd="btdownloadheadless.py")
class TestBtdownloadheadlessPy:
    @pytest.mark.complete("btdownloadheadless.py ")
    def test_1(self, completion):
        assert completion
