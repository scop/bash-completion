import pytest


class TestAwk(object):

    @pytest.mark.complete("awk ")
    def test_1(self, completion):
        assert completion.list
