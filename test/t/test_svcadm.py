import pytest


class TestSvcadm(object):

    @pytest.mark.complete("svcadm ")
    def test_1(self, completion):
        assert completion.list
