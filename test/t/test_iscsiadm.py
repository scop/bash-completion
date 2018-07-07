import pytest


class TestIscsiadm(object):

    @pytest.mark.complete("iscsiadm --mode")
    def test_1(self, completion):
        assert completion.list
