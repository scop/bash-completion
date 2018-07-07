import pytest


class TestPkgDelete(object):

    @pytest.mark.complete("pkg_delete ")
    def test_1(self, completion):
        assert completion.list
