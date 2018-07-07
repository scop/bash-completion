import pytest


class TestLftpget(object):

    @pytest.mark.complete("lftpget -")
    def test_1(self, completion):
        assert completion.list
