import pytest


@pytest.mark.bashcomp(pre_cmds=("PATH=/usr/lib/mailman/bin:$PATH",))
class TestChangePw:
    @pytest.mark.complete("change_pw -")
    def test_1(self, completion):
        assert completion
