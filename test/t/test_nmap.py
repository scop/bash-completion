import pytest


class TestNmap(object):

    @pytest.mark.complete("nmap --v")
    def test_1(self, completion):
        assert completion.list
