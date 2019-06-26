import pytest


@pytest.mark.bashcomp(cmd="munin-node-configure")
class TestMuninNodeConfigure:
    @pytest.mark.complete("munin-node-configure --libdir ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete(
        "munin-node-configure -",
        require_cmd=True,
        xfail=(
            "! (munin-node-configure --help 2>&1 || :) "
            "| command grep -q -- '[[:space:]]-'"
        ),
    )
    def test_2(self, completion):
        assert completion
