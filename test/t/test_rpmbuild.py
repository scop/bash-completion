import pytest


class TestRpmbuild(object):

    @pytest.mark.complete("rpmbuild -")
    def test_1(self, completion):
        assert completion.list
