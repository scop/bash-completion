import pytest


class Test(object):

    @pytest.mark.complete("mkfifo ")
    def test_(self, completion):
        assert completion.list
