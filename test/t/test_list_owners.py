import pytest


@pytest.mark.bashcomp(pre_cmds=("PATH=/usr/lib/mailman/bin:$PATH",))
class TestListOwners:
    @pytest.mark.complete("list_owners -")
    def test_1(self, completion):
        assert completion
