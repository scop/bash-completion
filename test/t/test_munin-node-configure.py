import pytest


class Test(object):

    @pytest.mark.complete("munin-node-configure --libdir ")
    def test_libdir(self, completion):
        assert completion.list
