import pytest


@pytest.mark.bashcomp(cmd="lintian-info")
class TestLintianInfo:
    @pytest.mark.complete("lintian-info ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("lintian-info --", require_cmd=True)
    def test_2(self, completion):
        assert completion
