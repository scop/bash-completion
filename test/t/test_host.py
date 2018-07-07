import pytest


class TestHost(object):

    @pytest.mark.complete("host -")
    def test_1(self, completion):
        assert completion.list
