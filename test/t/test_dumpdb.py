import pytest


@pytest.mark.bashcomp(pre_cmds=("PATH=/usr/lib/mailman/bin:$PATH",))
class TestDumpdb:
    @pytest.mark.complete("dumpdb ")
    def test_1(self, completion):
        assert completion
