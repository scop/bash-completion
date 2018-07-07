import pytest


class TestMkinitrd(object):

    @pytest.mark.complete("mkinitrd ")
    def test_1(self, completion):
        assert completion.list
