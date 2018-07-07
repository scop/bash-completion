import pytest


class TestNtpdate(object):

    @pytest.mark.complete("ntpdate -")
    def test_1(self, completion):
        assert completion.list
