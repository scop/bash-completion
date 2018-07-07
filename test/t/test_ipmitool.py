import pytest


class TestIpmitool(object):

    @pytest.mark.complete("ipmitool ")
    def test_1(self, completion):
        assert completion.list
