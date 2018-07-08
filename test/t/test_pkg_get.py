import pytest


class TestPkgGet(object):

    @pytest.mark.complete("pkg-get ")
    def test_1(self, completion):
        assert completion.list
