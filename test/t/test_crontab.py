import pytest


class Test(object):

    @pytest.mark.complete("crontab ")
    def test_(self, completion):
        assert completion.list
