import pytest


class TestGrub(object):

    @pytest.mark.complete("grub --")
    def test_1(self, completion):
        assert completion.list
