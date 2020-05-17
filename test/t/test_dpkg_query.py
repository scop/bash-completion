import pytest


@pytest.mark.bashcomp(cmd="dpkg-query",)
class TestDpkgQuery:
    @pytest.mark.complete("dpkg-query --", require_cmd=True)
    def test_options(self, completion):
        assert completion

    @pytest.mark.complete("dpkg-query -W dpk", require_cmd=True)
    def test_show(self, completion):
        assert "dpkg" in completion
