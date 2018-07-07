import pytest


class TestLusermod(object):

    @pytest.mark.complete("lusermod ")
    def test_1(self, completion):
        assert completion.list
