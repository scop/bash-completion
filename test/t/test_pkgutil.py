import pytest


class TestPkgutil(object):

    @pytest.mark.complete("pkgutil ")
    def test_1(self, completion):
        assert completion.list
