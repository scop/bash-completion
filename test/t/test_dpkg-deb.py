import pytest


class Test(object):

    @pytest.mark.complete("dpkg-deb --c")
    def test_c(self, completion):
        assert completion.list
