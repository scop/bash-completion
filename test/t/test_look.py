import subprocess

import pytest


class TestLook:
    @pytest.mark.complete("look foo")
    def test_1(self, completion):
        try:
            subprocess.check_call(
                "look foo 2>/dev/null | command grep -q ^foo", shell=True
            )
        except BaseException:
            assert not completion
        else:
            assert completion
