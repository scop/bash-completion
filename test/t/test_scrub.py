import pytest


class TestScrub:
    @pytest.mark.complete("scrub ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("scrub -", require_cmd=True)
    def test_2(self, completion):
        assert completion

    # Not all scrub versions list available patterns in --help output
    @pytest.mark.complete(
        "scrub -p ",
        xfail="! (scrub --help 2>&1 || :) | command grep -q ^Available",
    )
    def test_3(self, completion):
        assert completion
