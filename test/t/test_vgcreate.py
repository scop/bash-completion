import pytest


class Test(object):

    @pytest.mark.complete("vgcreate -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("vgcreate __does_not_exist__")
    def test_nonexistent(self, completion):
        assert not completion.list
