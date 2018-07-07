import pytest


class TestEject(object):

    @pytest.mark.complete("eject -")
    def test_1(self, completion):
        assert completion.list
