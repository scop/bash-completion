import pytest


@pytest.mark.bashcomp(ignore_env=r"^[+-]_comp_cmd_scp__path_esc=")
class TestRsync:
    @pytest.mark.complete("rsync ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("rsync --rsh ")
    def test_2(self, completion):
        assert completion == "rsh ssh".split()

    @pytest.mark.complete("rsync --rsh=")
    def test_3(self, completion):
        assert completion == "rsh ssh".split()

    @pytest.mark.complete("rsync --", require_cmd=True)
    def test_4(self, completion):
        assert "--help" in completion
