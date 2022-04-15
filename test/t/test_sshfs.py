import pytest


@pytest.mark.bashcomp(ignore_env=r"^[+-]_comp_cmd_scp__path_esc=")
class TestSshfs:
    @pytest.mark.complete("sshfs ./")
    def test_1(self, completion):
        assert completion
