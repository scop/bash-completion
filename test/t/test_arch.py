import pytest


@pytest.mark.bashcomp(pre_cmds=("PATH=/usr/lib/mailman/bin:$PATH",))
class TestArch:
    @pytest.mark.complete("arch -", require_cmd=True)
    def test_1(self, completion):
        assert completion
