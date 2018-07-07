import pytest


class TestFreebsdUpdate(object):

    @pytest.mark.complete("freebsd-update ")
    def test_1(self, completion):
        assert completion.list
