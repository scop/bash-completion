import pytest


class Test(object):

    @pytest.mark.complete("userdel -")
    def test_dash(self, completion):
        assert completion.list

    @pytest.mark.complete("userdel root")
    def test_root(self, completion):
        assert "root" in completion.list
