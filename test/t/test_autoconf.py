import pytest


class TestAutoconf(object):

    @pytest.mark.complete("autoconf ")
    def test_1(self, completion):
        assert completion.list
