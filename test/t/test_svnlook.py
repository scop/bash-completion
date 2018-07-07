import pytest


class TestSvnlook(object):

    @pytest.mark.complete("svnlook ")
    def test_1(self, completion):
        assert completion.list
