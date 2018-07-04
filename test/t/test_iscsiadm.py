import pytest


class Test(object):

    @pytest.mark.complete("iscsiadm --mode")
    def test_mode(self, completion):
        assert completion.list
