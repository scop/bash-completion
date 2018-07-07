import pytest


class TestAutoreconf(object):

    @pytest.mark.complete("autoreconf ")
    def test_1(self, completion):
        assert completion.list
