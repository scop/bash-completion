import pytest


class Test(object):

    @pytest.mark.complete("nmap --v")
    def test_v(self, completion):
        assert completion.list
