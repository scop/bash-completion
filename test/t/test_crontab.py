import pytest


class TestCrontab(object):

    @pytest.mark.complete("crontab ")
    def test_1(self, completion):
        assert completion.list
