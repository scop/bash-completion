import pytest


class TestSvn:
    @pytest.mark.complete("svn ")
    def test_1(self, completion):
        assert completion
