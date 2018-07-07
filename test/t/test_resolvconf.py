import pytest


class TestResolvconf(object):

    @pytest.mark.complete("resolvconf -")
    def test_1(self, completion):
        assert completion.list
