import pytest


@pytest.mark.bashcomp(pre_cmds=("PATH=/usr/lib/mailman/bin:$PATH",))
class TestMailmanctl:
    @pytest.mark.complete("mailmanctl ")
    def test_1(self, completion):
        assert completion
