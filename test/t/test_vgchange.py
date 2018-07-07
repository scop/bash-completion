import pytest


class TestVgchange(object):

    @pytest.mark.complete("vgchange -")
    def test_1(self, completion):
        assert completion.list
