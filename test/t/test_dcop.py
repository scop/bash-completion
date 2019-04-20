import subprocess

import pytest


class TestDcop:
    @pytest.mark.complete("dcop ")
    def test_1(self, completion):
        try:
            subprocess.check_call("dcop &>/dev/null", shell=True)
        except BaseException:
            assert not completion
        else:
            assert completion
