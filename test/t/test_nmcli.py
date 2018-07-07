import pytest


class TestNmcli(object):

    @pytest.mark.complete("nmcli ")
    def test_1(self, completion):
        assert completion.list
