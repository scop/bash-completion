import os

import pytest


class TestTime:
    @pytest.mark.complete("time set")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("time -p find -typ")
    def test_2(self, completion):
        assert completion  # find's options

    @pytest.mark.complete("time shared/bin/")
    def test_3(self, completion):
        execs = sorted(
            x
            for x in os.listdir("shared/bin")
            if os.path.isfile("shared/bin/%s" % x)
            and os.access("shared/bin/%s" % x, os.X_OK)
        )
        assert completion == execs
