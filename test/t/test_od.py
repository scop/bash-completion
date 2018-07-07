import pytest


class TestOd(object):

    @pytest.mark.complete("od ")
    def test_1(self, completion):
        assert completion.list
