import pytest


class TestUmount(object):

    @pytest.mark.complete("umount ")
    def test_1(self, completion):
        assert completion.list
