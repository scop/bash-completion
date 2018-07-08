import pytest


@pytest.mark.bashcomp(
    pre_cmds=(
        "PATH=/usr/lib/mailman/bin:$PATH",
    ),
)
class TestCleanarch(object):

    @pytest.mark.complete("cleanarch -")
    def test_1(self, completion):
        assert completion.list
