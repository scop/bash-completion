import pytest


class TestIonice(object):

    @pytest.mark.complete("ionice -")
    def test_1(self, completion):
        assert completion.list
