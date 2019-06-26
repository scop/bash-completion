import pytest


@pytest.mark.bashcomp(cmd="slapt-src")
class TestSlaptSrc:
    @pytest.mark.complete("slapt-src -", require_cmd=True)
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("slapt-src --bu", require_cmd=True)
    def test_2(self, completion):
        assert completion == "--build"

    @pytest.mark.complete("slapt-src --ins", require_cmd=True)
    def test_3(self, completion):
        assert completion == "--install"
