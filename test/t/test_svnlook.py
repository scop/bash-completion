import pytest


class TestSvnlook:
    @pytest.mark.complete("svnlook ")
    def test_1(self, completion):
        assert completion
