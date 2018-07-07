import pytest


class TestStrace(object):

    @pytest.mark.complete("strace -")
    def test_1(self, completion):
        assert completion.list
