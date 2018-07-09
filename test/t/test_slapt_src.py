import pytest


@pytest.mark.bashcomp(
    cmd="slapt-src",
)
class TestSlaptSrc(object):

    @pytest.mark.complete("slapt-src -")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("slapt-src --bu")
    def test_2(self, completion):
        assert completion.list == ["--build"]

    @pytest.mark.complete("slapt-src --ins")
    def test_3(self, completion):
        assert completion.list == ["--install"]
