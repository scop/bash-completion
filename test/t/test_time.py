import os

import pytest


class TestTime:
    @pytest.mark.complete("time _comp_delimite", cwd="shared/empty_dir")
    def test_command(self, completion):
        """
        Test completion of commands.

        We use a function of ours as the test subject, as that's guaranteed
        to be available, and do not rely on anything in particular in $PATH.
        """
        assert completion == "d" or "_comp_delimited" in completion

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
