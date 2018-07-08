import subprocess

import pytest


class TestLook(object):

    @pytest.mark.complete("look foo")
    def test_1(self, bash, completion):
        try:
            subprocess.check_call(
                "look foo 2>/dev/null | command grep -q ^foo", shell=True)
        except BaseException:
            assert not completion.list
        else:
            assert completion.list
