import pytest


class TestSshKeygen(object):

    @pytest.mark.complete("ssh-keygen -")
    def test_1(self, completion):
        assert completion.list
