import pytest


class Test(object):

    @pytest.mark.complete("grub --")
    def test_dash(self, completion):
        assert completion.list
