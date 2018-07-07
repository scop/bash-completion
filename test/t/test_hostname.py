import pytest


class TestHostname(object):

    @pytest.mark.complete("hostname -")
    def test_1(self, completion):
        assert completion.list
