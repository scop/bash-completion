import pytest


@pytest.mark.bashcomp(cmd="munin-node-configure")
class TestMuninNodeConfigure:
    @pytest.mark.complete("munin-node-configure --libdir ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("munin-node-configure -")
    def test_2(self, completion):
        assert completion
