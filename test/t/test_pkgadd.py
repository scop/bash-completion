import pytest


class TestPkgadd(object):

    @pytest.mark.complete("pkgadd ")
    def test_1(self, completion):
        assert completion.list
