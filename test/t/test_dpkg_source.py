import pytest


class TestDpkgSource(object):

    @pytest.mark.complete("dpkg-source -")
    def test_1(self, completion):
        assert completion.list
