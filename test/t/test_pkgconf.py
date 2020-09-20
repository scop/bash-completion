import pytest


@pytest.mark.bashcomp(cmd="pkgconf")
class TestPkgconf:
    @pytest.mark.complete("pkgconf ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("pkgconf -", require_cmd=True)
    def test_2(self, completion):
        assert completion
