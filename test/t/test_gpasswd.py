import pytest


class TestGpasswd(object):

    @pytest.mark.complete("gpasswd ")
    def test_1(self, completion):
        assert completion.list
