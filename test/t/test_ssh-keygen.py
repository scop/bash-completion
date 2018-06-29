import pytest


class Test(object):

    @pytest.mark.complete("ssh-keygen -")
    def test_dash(self, completion):
        assert completion.list
