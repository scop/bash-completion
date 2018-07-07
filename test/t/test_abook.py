import pytest


class TestAbook(object):

    @pytest.mark.complete("abook -")
    def test_1(self, completion):
        assert completion.list
