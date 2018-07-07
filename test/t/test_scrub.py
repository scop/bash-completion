import pytest


class Test(object):

    @pytest.mark.complete("scrub ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("scrub -")
    def test_dash(self, completion):
        assert completion.list

    # Not all scrub versions list available patterns in --help output
    @pytest.mark.complete("scrub -p ",
                          skipif="(scrub 2>&1 --help || :) | "
                          "! command grep -q ^Available")
    def test_p(self, completion):
        assert completion.list
