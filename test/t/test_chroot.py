import pytest


class TestChroot(object):

    @pytest.mark.complete("chroot ")
    def test_1(self, completion):
        assert completion.list
