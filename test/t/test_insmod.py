import pytest


class TestInsmod(object):

    @pytest.mark.complete("insmod ")
    def test_1(self, completion):
        assert completion.list
