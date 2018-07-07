import pytest


class TestLintian(object):

    @pytest.mark.complete("lintian --")
    def test_1(self, completion):
        assert completion.list
