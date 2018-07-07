import pytest


class TestSvn(object):

    @pytest.mark.complete("svn ")
    def test_1(self, completion):
        assert completion.list
