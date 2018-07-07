import pytest


class TestScrub(object):

    @pytest.mark.complete("scrub ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("scrub -")
    def test_2(self, completion):
        assert completion.list

    # Not all scrub versions list available patterns in --help output
    @pytest.mark.complete("scrub -p ",
                          skipif="(scrub 2>&1 --help || :) | "
                          "! command grep -q ^Available")
    def test_3(self, completion):
        assert completion.list
