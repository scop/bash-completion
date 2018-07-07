import pytest


class TestSmbget(object):

    @pytest.mark.complete("smbget -")
    def test_1(self, completion):
        assert completion.list
