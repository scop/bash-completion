import pytest


class TestSmbcquotas(object):

    @pytest.mark.complete("smbcquotas -")
    def test_1(self, completion):
        assert completion.list
