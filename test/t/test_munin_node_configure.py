import pytest


class TestMuninNodeConfigure(object):

    @pytest.mark.complete("munin-node-configure --libdir ")
    def test_1(self, completion):
        assert completion.list
