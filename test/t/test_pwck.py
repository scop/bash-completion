import pytest


class TestPwck(object):

    @pytest.mark.complete("pwck ")
    def test_1(self, completion):
        assert completion.list
