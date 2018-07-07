import pytest


class TestDpkgDeb(object):

    @pytest.mark.complete("dpkg-deb --c")
    def test_1(self, completion):
        assert completion.list
