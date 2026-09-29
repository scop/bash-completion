import pytest


@pytest.mark.bashcomp(pre_cmds=("PATH=/usr/lib/mailman/bin:$PATH",))
class TestGenaliases:
    @pytest.mark.complete("genaliases -")
    def test_1(self, completion):
        assert completion
