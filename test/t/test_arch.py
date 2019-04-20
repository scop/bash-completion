import pytest


@pytest.mark.bashcomp(pre_cmds=("PATH=/usr/lib/mailman/bin:$PATH",))
class TestArch:
    @pytest.mark.complete("arch -")
    def test_1(self, completion):
        assert completion
