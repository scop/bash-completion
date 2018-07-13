import pytest


@pytest.mark.bashcomp(
    cmd="lintian-info",
)
class TestLintianInfo(object):

    @pytest.mark.complete("lintian-info ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("lintian-info --")
    def test_2(self, completion):
        assert completion.list
