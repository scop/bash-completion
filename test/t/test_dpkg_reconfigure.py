import pytest


class TestDpkgReconfigure(object):

    @pytest.mark.complete("dpkg-reconfigure --")
    def test_1(self, completion):
        assert completion.list
