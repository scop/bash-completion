import pytest


class TestHping3(object):

    @pytest.mark.complete("hping3 ")
    def test_1(self, completion):
        assert completion.list
