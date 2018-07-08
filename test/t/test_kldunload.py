import subprocess

import pytest


class TestKldunload(object):

    @pytest.mark.complete("kldunload ")
    def test_1(self, completion):
        try:
            subprocess.check_call(
                r"kldstat 2>/dev/null | command grep -q '\.ko$'", shell=True)
        except BaseException:
            assert not completion.list
        else:
            assert completion.list
