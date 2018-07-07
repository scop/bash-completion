import pytest


class TestChpasswd(object):

    @pytest.mark.complete("chpasswd -")
    def test_1(self, completion):
        assert completion.list
