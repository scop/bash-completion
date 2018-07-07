import pytest


class TestHwclock(object):

    @pytest.mark.complete("hwclock -")
    def test_1(self, completion):
        assert completion.list
